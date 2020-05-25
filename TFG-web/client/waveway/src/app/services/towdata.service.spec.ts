import { TestBed } from '@angular/core/testing';

import { TowdataService } from './towdata.service';

describe('TowdataService', () => {
  let service: TowdataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TowdataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
