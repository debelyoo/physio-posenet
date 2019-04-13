"""
-*- coding: utf-8 -*-
"""
import yaml
import os
import logging

import tensorflow as tf

SERVE_DIR = './served_model'
PB_FILE_NAME = 'model-mobilenet_v1_101.pb'
CONFIG_FILE_NAME = 'config.yaml'


def _load_graph(frozen_graph_path):
    """
    Utility function to load a graph from a .pb file
    
    :param str frozen_graph_path            : path to the .pb file of the frozen graph
    :return tf.Graph                        : the loaded graph
    """
    # We load the protobuf file from the disk and parse it to retrieve the un-serialized graph_def
    with tf.gfile.GFile(frozen_graph_path, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # Then, we can use again a convenient built-in function to import a graph_def into the
    # current default Graph
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(
            graph_def,
            input_map=None,
            return_elements=None,
            name='',
            producer_op_list=None,
        )
    return graph


def _load_output_stride(config_path_name):
    """
    Utility function to load the output stride. The output stride is used for ...
    
    :param str config_path_name             : path to the configuration file of the posenet model 
    :return int                             : the output stride 
    """
    cfg_f = open(config_path_name, "r+")
    cfg = yaml.load(cfg_f)
    output_stride = cfg['outputStride']

    return output_stride


def load_posenet_model(serve_dir=SERVE_DIR, pb_file_name=PB_FILE_NAME, config_file_name=CONFIG_FILE_NAME):
    """
    Function to load the posnet model output nodes and the output stride
    
    :param str serve_dir                    : the path to the serving directory of the model
    :param str pb_file_name                 : the name of the .pb file
    :param str config_file_name             : the name of configuration file
    :return tuple                           : the output stride and the model output nodes
    """

    # load the frozen model
    frozen_graph_path = os.path.join(serve_dir, pb_file_name)
    print("plop")
    print(frozen_graph_path)

    posnet_graph = _load_graph(frozen_graph_path)

    # create a temo session and retrieve the output nodes
    temp_sess = tf.Session(graph=posnet_graph)
    with temp_sess.as_default():
        offsets = posnet_graph.get_tensor_by_name('offset_2:0')
        displacement_fwd = posnet_graph.get_tensor_by_name('displacement_fwd_2:0')
        displacement_bwd = posnet_graph.get_tensor_by_name('displacement_bwd_2:0')
        heatmaps = posnet_graph.get_tensor_by_name('heatmap:0')

    # load the output stride
    config_path_name = os.path.join(serve_dir, config_file_name)
    output_stride = _load_output_stride(config_path_name)

    return output_stride, [heatmaps, offsets, displacement_fwd, displacement_bwd]
