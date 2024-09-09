#include <stdio.h>
#include <math.h>

typedef struct{
	float x;
	float y;
} Point;

typedef struct{
	int n_points;
	Point* points;
} Polygon;


float distance(Point p1, Point p2) {
	return pow(pow(p1.x-p2.x, 2) + pow(p1.y-p2.y, 2), 0.5);
}

float perimeter(Polygon* poly) {
	float out = 0;

	for (int i = 0; i < poly->n_points - 1; i++) {
		out += distance(poly->points[i], poly->points[i+1]);
	}
	out += distance(poly->points[0], poly->points[poly->n_points-1]);

	return out;
}

int main(){
	Polygon poly;
	scanf("%d",&poly.n_points);
	Point points[poly.n_points];
	for(int i=0;i<poly.n_points;i++){
		scanf("%f %f", &points[i].x,& points[i].y);
	}
	poly.points = points;
	printf("%.2f", perimeter(&poly));
}