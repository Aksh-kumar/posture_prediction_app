import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { URLConstant } from 'src/contstants/url.constants';
import { Observable } from 'rxjs';
import { PredictPostureClass, PredictPostureProbability,
   PredictPostureRequestPayload, PredictPosturesTest } from 'src/interface/predict-postures.interface';
@Injectable({
  providedIn: 'root'
})
export class PosturePredictService {

  // tslint:disable-next-line:variable-name
  constructor(private _httpClient: HttpClient) { }

  public getTest(): Observable<PredictPosturesTest> {
    return this._httpClient.get<PredictPosturesTest>(URLConstant.PREDICT_TEST_URL);
  }

  public getClassMapping(): Observable<{[key: number]: string}> {
    return this._httpClient.get<{[key: number]: string}>(URLConstant.CLASS_MAPPING_URL);
  }

  public postPredictPostureClass(payload: PredictPostureRequestPayload): Observable<PredictPostureClass> {
    return this._httpClient.post<PredictPostureClass>(URLConstant.PREDICT_CLASS_LABEL_URL, payload);
  }

  public postPredictPostureProbability(payload: PredictPostureRequestPayload): Observable<PredictPostureProbability[]> {
    return this._httpClient.post<PredictPostureProbability[]>(URLConstant.PREDICT_PROBABILITY_URL, payload);
  }
}
