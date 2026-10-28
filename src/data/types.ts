/**
 * Dimensions transcribed from SAAMI cartridge drawings. All lengths are inches and all
 * angles degrees. Tolerances (`*Tol`) are signed offsets from the nominal value, as SAAMI
 * states them (e.g. `rimDia: 0.394, rimDiaTol: -0.010`). Positions (`*At`) are measured
 * from the head of the case.
 */
export interface Cartridge {
  name: string;
  aliases: string[];
  category: "pistol" | "rifle" | "rimfire";
  standard: string;
  pdfPage: number;
  issued: string;
  revised?: string;
  rimType: "rimless" | "rimmed" | "semi-rimmed" | "rebated" | "belted";
  profile: "straight" | "bottleneck";

  rimDia: number;
  rimDiaTol?: number;
  /** Head to the front face of the rim. */
  rimThickness: number;
  rimThicknessTol?: number;
  /** Length of the cylindrical edge of the rim. */
  rimLand?: number;
  rimLandTol?: number;
  rimChamferDeg?: number;
  rimChamferTolDeg?: number;

  /** Extractor groove diameter; on rimmed cases, the reference diameter of the optional undercut. */
  grooveDia?: number;
  grooveDiaTol?: number;
  grooveWidth?: number;
  grooveWidthTol?: number;
  grooveAngleDeg?: number;
  grooveAngleTolDeg?: number;

  beltDia?: number;
  /** Head to the front of the belt. */
  beltLength?: number;
  beltLengthTol?: number;

  /** General tolerance for body diameters unless stated otherwise. */
  bodyDiaTol?: number;
  headDia: number;
  headDiaAt?: number;
  bodyDia2?: number;
  bodyDia2At?: number;
  mouthDia?: number;

  shoulderDia?: number;
  shoulderAt?: number;
  /** Absent for radiused (Weatherby venturi) shoulders. */
  shoulderAngleDeg?: number;
  datumDia?: number;
  datumAt?: number;
  datumAtTol?: number;
  neckDia?: number;
  neckAt?: number;

  caseLength: number;
  caseLengthTol?: number;
  bulletDia?: number;
  bulletDiaTol?: number;
  /** Lead bullet diameter, where SAAMI gives one separately. */
  bulletDiaLead?: number;
  bulletDiaLeadTol?: number;
  oalMin?: number;
  oalMax: number;
  notes?: string;
}

export interface Shotshell {
  name: string;
  category: "shotshell";
  standard: string;
  gauge: string;
  shellLength: string;
  barrel: string;
  pdfPage: number;
  issued: string;
  revised?: string;

  rimDia: number;
  rimDiaTol?: number;
  rimThickness: number;
  rimThicknessTol?: number;
  rimChamferDeg?: number;
  rimChamferBasicDia?: number;
  headDia: number;
  headDiaTol?: number;
  headDiaAt: number;
  mouthDia: number;
  mouthDiaTol?: number;
  /** General tolerance for the lengths below. */
  lengthTol?: number;
  lengthFolded?: number;
  lengthRolled: number;
  lengthUncrimped: number;
  lengthUncrimpedTol?: number;
  notes?: string;
}

export type Round = Cartridge | Shotshell;
