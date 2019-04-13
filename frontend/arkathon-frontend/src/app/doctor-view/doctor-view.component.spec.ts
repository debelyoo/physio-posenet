import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DoctorViewComponent } from './doctor-view.component';

describe('DoctorViewComponent', () => {
  let component: DoctorViewComponent;
  let fixture: ComponentFixture<DoctorViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DoctorViewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DoctorViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
