import { Component, OnInit } from '@angular/core';

export interface PeriodicElement {
  date: string;
  time: string;
  score: number;
}

const ELEMENT_DATA: PeriodicElement[] = [
  {time: '2pm', date: '02.02.2019', score: 86},
  {time: '6pm', date: '12.03.2019', score: 74},
  {time: '10am', date: '28.03.2019', score: 69},
  {time: '2pm', date: '11.04.2019', score: 91}
];

@Component({
  selector: 'app-exercise-table',
  templateUrl: './exercise-table.component.html',
  styleUrls: ['./exercise-table.component.css']
})
export class ExerciseTableComponent implements OnInit {

  displayedColumns: string[] = ['date', 'time', 'score'];
  dataSource = ELEMENT_DATA;

  constructor() { }

  ngOnInit() {
  }

}
