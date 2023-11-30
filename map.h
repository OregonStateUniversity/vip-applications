#ifndef VIP_APPLICATIONS_MAP_H

int map_int(int (*function)(int), int* source_iterable, int* dest_iterable, size_t length);
int map_char(char (*function)(char), char* source_iterable, char* dest_iterable, size_t length);
int map_float(float (*function)(float), float* source_iterable, float* dest_iterable, size_t length);

#define VIP_APPLICATIONS_MAP_H

#endif //VIP_APPLICATIONS_MAP_H
