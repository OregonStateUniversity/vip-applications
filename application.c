#include <stdio.h>
#include "map.h"

/* DESCRIPTION
 * Since C does not (at least easily) allow a way to pass arguments of an arbitrary
 * type to a function, I decided that the simplest course of action was to split
 * the map function into three separate map functions, each corresponding to a different
 * type. Each function is identical in implementation, and only differs in the type
 * of data it is able to manipulate. Each map function takes a function, applies
 * it to each element of an array of input data, and then stores the results in
 * an output array that is big enough to hold each result.
 *
 * PARAMETERS
 * type (*function)(type): Pointer to a function that takes an argument of a particular
 *                         type and returns a value of that same type.
 *
 * type* source_iterable:  Pointer to an array of values of a particular type that
 *                         will each be passed to the aforementioned function.
 *
 * type* dest_iterable:    Pointer to an array of values of a particular type that
 *                         will hold the results of applying the aforementioned
 *                         function to each of the values stored in source_iterable.
 *
 * size_t length:          Number of values to perform the operation on. Must be
 *                         less than or equal to the length of the shorter of the
 *                         two arrays.
 *
 * RETURN VALUE
 * Each function will return -1 if the operation was unsuccessful, otherwise it
 * will return 0.
 */
int map_int(int (*function)(int), int* source_iterable, int* dest_iterable, size_t length)
{
    if (length < 1) {
        fprintf(stderr, "Length must be positive.\n");
        return -1;
    }

    for (int i = 0; i < length; ++i)
    {
        dest_iterable[i] = function(source_iterable[i]);
    }
    return 0;
}

int map_char(char (*function)(char), char* source_iterable, char* dest_iterable, size_t length)
{
    if (length < 1) {
        fprintf(stderr, "Length must be positive.\n");
        return -1;
    }

    for (int i = 0; i < length; ++i)
    {
        dest_iterable[i] = function(source_iterable[i]);
    }
    return 0;
}

int map_float(float (*function)(float), float* source_iterable, float* dest_iterable, size_t length)
{
    if (length < 1) {
        fprintf(stderr, "Length must be positive.\n");
        return -1;
    }

    for (int i = 0; i < length; ++i)
    {
        dest_iterable[i] = function(source_iterable[i]);
    }
    return 0;
}