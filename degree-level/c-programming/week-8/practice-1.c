#include <stdio.h>

typedef struct {
    float x;
    float y;
} Point;

typedef struct {
    float mass;
    Point pos;
} Particle;


Point center_of_mass(Particle arr[], int n) {
    float sum_m = 0;
    Point out = {0.0, 0.0};
    Particle p;

    for (int i = 0; i < n; i++) {
        p = arr[i];

        sum_m += p.mass;
        out.x += p.mass * p.pos.x;
        out.y += p.mass * p.pos.y;
    }

    out.x /= sum_m;
    out.y /= sum_m;

    return out;
}


int main(){
    int n;
    scanf("%d",&n);
    Particle particles[n];
    for (int i=0; i<n; i++){
        scanf(
            "%f %f %f", 
            &particles[i].mass, 
            &particles[i].pos.x, 
            &particles[i].pos.y
        );
    }
    Point com = center_of_mass(particles,n);
    printf("%.2f %.2f",com.x,com.y);
}