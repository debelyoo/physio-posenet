import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ExerciseTableComponent } from './exercise-table.component';

describe('ExerciseTableComponent', () => {
  let component: ExerciseTableComponent;
  let fixture: ComponentFixture<ExerciseTableComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ExerciseTableComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ExerciseTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
