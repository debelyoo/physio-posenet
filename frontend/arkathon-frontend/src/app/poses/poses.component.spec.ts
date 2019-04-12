import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PosesComponent } from './poses.component';

describe('PosesComponent', () => {
  let component: PosesComponent;
  let fixture: ComponentFixture<PosesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PosesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PosesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
