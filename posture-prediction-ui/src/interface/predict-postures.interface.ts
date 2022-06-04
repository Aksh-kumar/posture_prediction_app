export interface PredictPosturesTest {
    msg: string;
}

export interface PredictPostureClass {
    class: number;
    class_name: string;
    probability_score: number;
}

export interface PredictPostureProbability {
    class: string;
    probability: number;
}

export interface PredictPostureRequestPayload {
        X0: number;
        Y0: number;
        Z0: number;
        X1: number;
        Y1: number;
        Z1: number;
        X2: number;
        Y2: number;
        Z2: number;
        X3?: number;
        Y3?: number;
        Z3?: number;
        X4?: number;
        Y4?: number;
        Z4?: number;
        X5?: number;
        Y5?: number;
        Z5?: number;
        X6?: number;
        Y6?: number;
        Z6?: number;
        X7?: number;
        Y7?: number;
        Z7?: number;
        X8?: number;
        Y8?: number;
        Z8?: number;
        X9?: number;
        Y9?: number;
        Z9?: number;
        X10?: number;
        Y10?: number;
        Z10?: number;
        X11?: number;
        Y11?: number;
        Z11?: number;
}

export interface SampleData {
    data: PredictPostureRequestPayload;
    label: number;
}

