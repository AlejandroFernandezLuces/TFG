import { TestBed } from '@angular/core/testing';

import { GraphDrawService } from './graph-draw.service';

describe('GraphDrawService', () => {
  let service: GraphDrawService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GraphDrawService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
