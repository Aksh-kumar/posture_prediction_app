import { AfterViewChecked, AfterViewInit, Component, OnDestroy, OnInit } from '@angular/core';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { Subscription } from 'rxjs';
import { PredictPostureClass, PredictPostureProbability,
  PredictPostureRequestPayload, PredictPosturesTest } from 'src/interface/predict-postures.interface';
import { PosturePredictService } from 'src/service/posture-predict.service';
import {sampleData} from '../../assets/test-dataset';
import { DialogBoxComponent } from '../dialog-box/dialog-box.component';

export interface ISampleData {
  data: PredictPostureRequestPayload;
  label: string;
  prediction: string;
}

@Component({
  selector: 'app-posture-prediction',
  templateUrl: './posture-prediction.component.html',
  styleUrls: ['./posture-prediction.component.css']
})
export class PosturePredictionComponent implements OnInit, OnDestroy {
  axis: string[] = [];
  subscription: Subscription = new Subscription();
  testData: ISampleData[] = [];
  classMapping: {[key: number]: string};

  constructor(private posturePredictService: PosturePredictService,
              private matDialog: MatDialog) { }

  ngOnInit() {
    this.axis = ['X0', 'Y0', 'Z0', 'X1', 'Y1', 'Z1', 'X2', 'Y2', 'Z2', 'X3', 'Y3', 'Z3',
    'X4', 'Y4', 'Z4', 'X5', 'Y5', 'Z5', 'X6', 'Y6', 'Z6', 'X7', 'Y7', 'Z7',
    'X8', 'Y8', 'Z8', 'X9', 'Y9', 'Z9', 'X10', 'Y10', 'Z10', 'X11', 'Y11',
    'Z11', 'actual', 'prediction'];

    this.subscription.add(
      this.posturePredictService.getTest().subscribe((response: PredictPosturesTest) => {
        console.log(response);
      })
    );

    this.subscription.add(
      this.posturePredictService.getClassMapping().subscribe((response: {[key: number]: string}) => {
        this.classMapping = response;
        this.initSampleData();
      })
    );
  }

  openDialog(data: PredictPostureProbability[]): void {
    const dialogConfig = new MatDialogConfig();
    dialogConfig.data = data;
    const dialogRef = this.matDialog.open(DialogBoxComponent, dialogConfig);
  }

  initSampleData() {
    this.testData = [];
    sampleData.map((data: any) => {
      const axialData: PredictPostureRequestPayload =  data.data as PredictPostureRequestPayload;
      const trueLabel: string = this.classMapping[data.label];
      const predicted: string  = null;
      this.testData.push({data: axialData, label: trueLabel, prediction: predicted} as ISampleData);
    });
  }

  getProbabilityValue(idx: number) {
    this.subscription.add(
      // tslint:disable-next-line:max-line-length
      this.posturePredictService.postPredictPostureProbability(this.testData[idx].data).subscribe((response: PredictPostureProbability[]) => {
        this.openDialog(response);
      })
    );
  }

  getPredictionValue(payload: PredictPostureRequestPayload, idx: number): void {
    this.subscription.add(
      this.posturePredictService.postPredictPostureClass(payload).subscribe((response: PredictPostureClass) => {
        this.testData[idx].prediction = response.class_name;
      })
    );
  }

  getAllPrediction(event: Event): void {
      this.testData.map((value: ISampleData) => {
        value.prediction = null;
     });

      this.testData.map((value: ISampleData, idx: number) => this.getPredictionValue(value.data, idx));
  }

  getPrediction(idx: number) {
    this.getPredictionValue(this.testData[idx].data, idx);
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}
