import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ElectrodesComponent } from './electrodes.component';

describe('ElectrodesComponent', () => {
  let component: ElectrodesComponent;
  let fixture: ComponentFixture<ElectrodesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ElectrodesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ElectrodesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
