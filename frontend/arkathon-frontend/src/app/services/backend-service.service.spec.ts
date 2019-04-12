import { TestBed } from '@angular/core/testing';

import { BackendServiceService } from './backend-service.service';

describe('BackendServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: BackendServiceService = TestBed.get(BackendServiceService);
    expect(service).toBeTruthy();
  });
});
