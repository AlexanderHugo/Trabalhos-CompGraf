int cx, cy;
float raios;
float raiom;
float raioh;
float diametror;

void setup() {
  size(900, 600);
  stroke(0);
  
  int raio = min(width, height) / 2;
  raios = raio * 0.80;
  raiom = raio * 0.70;
  raioh = raio * 0.60;
  diametror = raio * 1.8;
  
  cx = width / 2;
  cy = height / 2;
}

void draw() {
  background(100);
  
  fill(12, 50, 12);
  ellipse(cx, cy, diametror, diametror);
  
  // A função Map() mapeia um range em outro. o primeiro parâmetro é o valor atual do sistema em segundos, o segundo é range inferior do valor atual e o terceiro é o superior. O quarto e o quinto são limite inferior e superior do novo mapeamento.
  float s = map(second(), 0, 60, 0, TWO_PI) - HALF_PI;
  float m = map(minute() + norm(second(), 0, 60), 0, 60, 0, TWO_PI) - HALF_PI; 
  float h = map(hour() + norm(minute(), 0, 60), 0, 24, 0, TWO_PI * 2) - HALF_PI;
  
  stroke(48, 200, 48);
  strokeWeight(1);
  line(cx, cy, cx + cos(s) * raios, cy + sin(s) * raios);
  strokeWeight(2);
  line(cx, cy, cx + cos(m) * raiom, cy + sin(m) * raiom);
  strokeWeight(4);
  line(cx, cy, cx + cos(h) * raioh, cy + sin(h) * raioh);
  
  strokeWeight(2);
  beginShape(POINTS);
  for (int a = 0; a < 360; a+=6) {
    float ang = radians(a);
    float x = cx + cos(ang) * raios;
    float y = cy + sin(ang) * raios;
    vertex(x, y);
  }
  endShape();
}
