import { TestBed } from '@angular/core/testing';

import { PosturePredictService } from './posture-predict.service';

describe('PosturePredict.Service.TsService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: PosturePredictService = TestBed.get(PosturePredictService);
    expect(service).toBeTruthy();
  });
});
