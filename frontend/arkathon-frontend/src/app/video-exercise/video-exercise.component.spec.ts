import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VideoExerciseComponent } from './video-exercise.component';

describe('VideoExerciseComponent', () => {
  let component: VideoExerciseComponent;
  let fixture: ComponentFixture<VideoExerciseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VideoExerciseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VideoExerciseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
