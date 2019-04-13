import { Component, OnInit } from '@angular/core';
import { ChartOptions, ChartType, ChartDataSets } from 'chart.js';
import { Label } from 'ng2-charts';

@Component({
  selector: 'app-gamification',
  templateUrl: './gamification.component.html',
  styleUrls: ['./gamification.component.css']
})
export class GamificationComponent implements OnInit {
  public lineChartOptions: ChartOptions = {
    responsive: false,
    legend: {
      display: true
    },
    scales: {
      xAxes: [
        {
          ticks: {
          beginAtZero: true
        },
        scaleLabel: {
          display: true,
                    
        }
      }],
      yAxes: [
        {
          ticks: {
          beginAtZero: true
        }
      }
      ]
    },
  };

  public lineChartType: ChartType = 'line';
  public lineChartLabels: Label[] = ['02.02.2019', '15.02.2019', '05.03.2019', '06.03.2019', '10.03.2019', '28.03.2019', '10.04.2019'];

  public lineChartData: ChartDataSets[] = [
    { 
      data: [
        65, 59, 80, 81, 56, 55, 40
      ],
      fill: false,
      label: 'Score',
    }
  ];

  public barChartOptions: ChartOptions = {
    responsive: false,
    legend: {
      display: true
    },
    scales: {
      xAxes: [
        {
          ticks: {
          beginAtZero: true
        },
        scaleLabel: {
          display: true,
                    
        }
      }],
      yAxes: [
        {
          ticks: {
          beginAtZero: true
        }
      }
      ]
    },
  };

  public barChartType: ChartType = 'bar';
  public barChartLabels: Label[] = ['Exercise 1', 'Exercise 2', 'Exercise 3', 'Exercise 4', 'Exercise 5', 'Exercise 6', 'Exercise 7'];

  public barChartData: ChartDataSets[] = [
    { 
      data: [
        5, 4, 18, 3, 25, 12, 10
      ],
      fill: false,
      label: 'Frequency',
    }
  ];

  public pieChartOptions: ChartOptions = {
    responsive: false,
    legend: {
      display: true
    },
    scales: {
      xAxes: [
        {
          display: false
        }
      ],
      yAxes: [
        { 
          display: false
        }
      ]
    },
  };

  public pieChartType: ChartType = 'doughnut';
  public pieChartLabels: Label[] = ['January 19', 'February 19', 'March 19', 'December 18', 'June 18', 'August 18', 'November 18'];
  public pieChartData: ChartDataSets[] = [
    { 
      data: [
        5, 4, 18, 3, 25, 12, 10
      ],
      fill: false,
    }
  ];

  constructor() { }

  ngOnInit() {
  }
}
