import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PosturePredictionComponent } from './posture-prediction.component';

describe('PosturePredictionComponent', () => {
  let component: PosturePredictionComponent;
  let fixture: ComponentFixture<PosturePredictionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PosturePredictionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PosturePredictionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
