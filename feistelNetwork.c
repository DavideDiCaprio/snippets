/*

*/

#include <stdio.h>
#include <stdint.h>

uint8_t non_linear(uint8_t x){
    return ((x<<1) | (x>>3) * 7) + (x&93);
}

void fn_round(uint8_t *p) {
    uint8_t l = p[0];
    uint8_t r = p[1];

    uint8_t new_l = r;
    uint8_t new_r = l ^ (non_linear(r));

    p[0] = new_l;
    p[1] = new_r;

}

void fn_deround(uint8_t *p) {
    uint8_t l = p[0];
    uint8_t r = p[1];

    uint8_t old_r = l;
    uint8_t old_l = r ^ (non_linear(l));

    p[0] = old_l;
    p[1] = old_r;

}

int main(void) {
    uint16_t n = 123;
    uint8_t *p = (uint8_t*) &n;

    printf("%d\n", n);
    fn_round(p);
    printf("%d\n", n);
    fn_deround(p);
    printf("%d\n", n);

    return 0;

}