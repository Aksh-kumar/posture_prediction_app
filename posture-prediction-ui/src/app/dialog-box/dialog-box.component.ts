import { Component, Inject, OnInit } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { PredictPostureProbability } from 'src/interface/predict-postures.interface';

@Component({
  selector: 'app-dialog-box',
  templateUrl: './dialog-box.component.html',
  styleUrls: ['./dialog-box.component.css']
})
export class DialogBoxComponent implements OnInit {
  dataSource: PredictPostureProbability[] = [];
  displayedColumns: string[] = ['class', 'probability'];
  constructor(@Inject(MAT_DIALOG_DATA) public data: PredictPostureProbability[],
              public dialogRef: MatDialogRef<DialogBoxComponent>) { }

  ngOnInit() {
    this.dataSource = this.data;
  }

  close() {
    this.dialogRef.close();
  }

}
