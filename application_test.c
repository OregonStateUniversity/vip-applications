#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include "application.c"

#define EPSILON 0.001

int add_two(int element)
{
    return element + 2;
}

int subtract_two(int element)
{
    return element - 2;
}

int multiply_by_two(int element)
{
    return element * 2;
}

int divide_by_two(int element)
{
    return element / 2;
}

int ints_are_equal(int (*function)(int), int* source_iterable, int* dest_iterable, size_t length)
{
    int result = 1;
    for (int i = 0; i < length; ++i) {
        if (function(source_iterable[i]) != dest_iterable[i]) {
            result = 0;
            break;
        }
    }
    return result;
}

char add_three(char element)
{
    return (element + 3) % 95 + 32;
}

char subtract_three(char element)
{
    return (element - 3) % 95 + 32;
}

char multiply_by_three(char element)
{
    return (element * 3) % 95 + 32;
}

char divide_by_three(char element)
{
    return (element / 3) % 95 + 32;
}

int chars_are_equal(char (*function)(char), char* source_iterable, char* dest_iterable, size_t length)
{
    int result = 1;
    for (int i = 0; i < length; ++i) {
        if (function(source_iterable[i]) != dest_iterable[i]) {
            result = 0;
            break;
        }
    }
    return result;
}

char rand_char()
{
    return ((unsigned)rand() % 95) + 32;
}

float add_four(float element)
{
    return element + 4.0f;
}

float subtract_four(float element)
{
    return element - 4.0f;
}

float multiply_by_four(float element)
{
    return element * 4.0f;
}

float divide_by_four(float element)
{
    return element / 4.0f;
}

int floats_are_equal(float (*function)(float), float* source_iterable, float* dest_iterable, size_t length)
{
    int result = 1;
    for (int i = 0; i < length; ++i) {
        if (fabsf(function(source_iterable[i]) - dest_iterable[i]) > EPSILON) {
            result = 0;
            break;
        }
    }
    return result;
}

void test_map_int()
{
    fprintf(stderr, "------------------------ TEST: map_int() -----------------------\n");

    // 1. Array size 0
    int test_source_1[0];
    int test_dest_1[0];

    int result = map_int(add_two, test_source_1, test_dest_1, 0);
    fprintf(stderr, "1. %s: Array size 0, add_two\n", result != -1 ? "FAILED" : "PASSED");

    result = map_int(subtract_two, test_source_1, test_dest_1, 0);
    fprintf(stderr, "1. %s: Array size 0, subtract_two\n", result != -1 ? "FAILED" : "PASSED");

    result = map_int(multiply_by_two, test_source_1, test_dest_1, 0);
    fprintf(stderr, "1. %s: Array size 0, multiply_by_two\n", result != -1 ? "FAILED" : "PASSED");

    result = map_int(divide_by_two, test_source_1, test_dest_1, 0);
    fprintf(stderr, "1. %s: Array size 0, divide_by_two\n", result != -1 ? "FAILED" : "PASSED");

    // 2. Array size 1
    int test_source_2[1] = {rand()};
    int test_dest_2[1];

    map_int(add_two, test_source_2, test_dest_2, 1);
    result = ints_are_equal(add_two, test_source_2, test_dest_2, 1);
    fprintf(stderr, "2. %s: Array size 1, add_two\n", result != 1 ? "FAILED" : "PASSED");

    map_int(subtract_two, test_source_2, test_dest_2, 1);
    result = ints_are_equal(subtract_two, test_source_2, test_dest_2, 1);
    fprintf(stderr, "2. %s: Array size 1, subtract_two\n", result != 1 ? "FAILED" : "PASSED");

    map_int(multiply_by_two, test_source_2, test_dest_2, 1);
    result = ints_are_equal(multiply_by_two, test_source_2, test_dest_2, 1);
    fprintf(stderr, "2. %s: Array size 1, multiply_by_two\n", result != 1 ? "FAILED" : "PASSED");

    map_int(divide_by_two, test_source_2, test_dest_2, 1);
    result = ints_are_equal(divide_by_two, test_source_2, test_dest_2, 1);
    fprintf(stderr, "2. %s: Array size 1, divide_by_two\n", result != 1 ? "FAILED" : "PASSED");

    // 3. Array size 2
    int test_source_3[2] = {rand(), rand()};
    int test_dest_3[2];

    map_int(add_two, test_source_3, test_dest_3, 2);
    result = ints_are_equal(add_two, test_source_3, test_dest_3, 2);
    fprintf(stderr, "3. %s: Array size 2, add_two\n", result != 1 ? "FAILED" : "PASSED");

    map_int(subtract_two, test_source_3, test_dest_3, 2);
    result = ints_are_equal(subtract_two, test_source_3, test_dest_3, 2);
    fprintf(stderr, "3. %s: Array size 2, subtract_two\n", result != 1 ? "FAILED" : "PASSED");

    map_int(multiply_by_two, test_source_3, test_dest_3, 2);
    result = ints_are_equal(multiply_by_two, test_source_3, test_dest_3, 2);
    fprintf(stderr, "3. %s: Array size 2, multiply_by_two\n", result != 1 ? "FAILED" : "PASSED");

    map_int(divide_by_two, test_source_3, test_dest_3, 2);
    result = ints_are_equal(divide_by_two, test_source_3, test_dest_3, 2);
    fprintf(stderr, "3. %s: Array size 2, divide_by_two\n", result != 1 ? "FAILED" : "PASSED");

    // 4. Array size 500
    int test_source_4[500];
    for (int i = 0; i < 500; ++i)
        test_source_4[i] = rand();
    int test_dest_4[500];

    map_int(add_two, test_source_4, test_dest_4, 500);
    result = ints_are_equal(add_two, test_source_4, test_dest_4, 500);
    fprintf(stderr, "4. %s: Array size 500, add_two\n", result != 1 ? "FAILED" : "PASSED");

    map_int(subtract_two, test_source_4, test_dest_4, 500);
    result = ints_are_equal(subtract_two, test_source_4, test_dest_4, 500);
    fprintf(stderr, "4. %s: Array size 500, subtract_two\n", result != 1 ? "FAILED" : "PASSED");

    map_int(multiply_by_two, test_source_4, test_dest_4, 500);
    result = ints_are_equal(multiply_by_two, test_source_4, test_dest_4, 500);
    fprintf(stderr, "4. %s: Array size 500, multiply_by_two\n", result != 1 ? "FAILED" : "PASSED");

    map_int(divide_by_two, test_source_4, test_dest_4, 500);
    result = ints_are_equal(divide_by_two, test_source_4, test_dest_4, 500);
    fprintf(stderr, "4. %s: Array size 500, divide_by_two\n", result != 1 ? "FAILED" : "PASSED");

    fprintf(stderr, "\n");

}

void test_map_char()
{
    fprintf(stderr, "------------------------ TEST: map_char() ----------------------\n");

    // 1. Array size 0
    char test_source_1[0];
    char test_dest_1[0];

    int result = map_char(add_three, test_source_1, test_dest_1, 0);
    fprintf(stderr, "1. %s: Array size 0, add_three\n", result != -1 ? "FAILED" : "PASSED");

    result = map_char(subtract_three, test_source_1, test_dest_1, 0);
    fprintf(stderr, "1. %s: Array size 0, subtract_three\n", result != -1 ? "FAILED" : "PASSED");

    result = map_char(multiply_by_three, test_source_1, test_dest_1, 0);
    fprintf(stderr, "1. %s: Array size 0, multiply_by_three\n", result != -1 ? "FAILED" : "PASSED");

    result = map_char(divide_by_three, test_source_1, test_dest_1, 0);
    fprintf(stderr, "1. %s: Array size 0, divide_by_three\n", result != -1 ? "FAILED" : "PASSED");

    // 2. Array size 1
    char test_source_2[1] = {rand_char()};
    char test_dest_2[1];

    map_char(add_three, test_source_2, test_dest_2, 1);
    result = chars_are_equal(add_three, test_source_2, test_dest_2, 1);
    fprintf(stderr, "2. %s: Array size 1, add_three\n", result != 1 ? "FAILED" : "PASSED");

    map_char(subtract_three, test_source_2, test_dest_2, 1);
    result = chars_are_equal(subtract_three, test_source_2, test_dest_2, 1);
    fprintf(stderr, "2. %s: Array size 1, subtract_three\n", result != 1 ? "FAILED" : "PASSED");

    map_char(multiply_by_three, test_source_2, test_dest_2, 1);
    result = chars_are_equal(multiply_by_three, test_source_2, test_dest_2, 1);
    fprintf(stderr, "2. %s: Array size 1, multiply_by_three\n", result != 1 ? "FAILED" : "PASSED");

    map_char(divide_by_three, test_source_2, test_dest_2, 1);
    result = chars_are_equal(divide_by_three, test_source_2, test_dest_2, 1);
    fprintf(stderr, "2. %s: Array size 1, divide_by_three\n", result != 1 ? "FAILED" : "PASSED");

    // 3. Array size 2
    char test_source_3[2] = {rand_char(), rand_char()};
    char test_dest_3[2];

    map_char(add_three, test_source_3, test_dest_3, 2);
    result = chars_are_equal(add_three, test_source_3, test_dest_3, 2);
    fprintf(stderr, "3. %s: Array size 2, add_three\n", result != 1 ? "FAILED" : "PASSED");

    map_char(subtract_three, test_source_3, test_dest_3, 2);
    result = chars_are_equal(subtract_three, test_source_3, test_dest_3, 2);
    fprintf(stderr, "3. %s: Array size 2, subtract_three\n", result != 1 ? "FAILED" : "PASSED");

    map_char(multiply_by_three, test_source_3, test_dest_3, 2);
    result = chars_are_equal(multiply_by_three, test_source_3, test_dest_3, 2);
    fprintf(stderr, "3. %s: Array size 2, multiply_by_three\n", result != 1 ? "FAILED" : "PASSED");

    map_char(divide_by_three, test_source_3, test_dest_3, 2);
    result = chars_are_equal(divide_by_three, test_source_3, test_dest_3, 2);
    fprintf(stderr, "3. %s: Array size 2, divide_by_three\n", result != 1 ? "FAILED" : "PASSED");

    // 4. Array size 500
    char test_source_4[500];
    for (int i = 0; i < 500; ++i)
        test_source_4[i] = rand_char();
    char test_dest_4[500];

    map_char(add_three, test_source_4, test_dest_4, 500);
    result = chars_are_equal(add_three, test_source_4, test_dest_4, 500);
    fprintf(stderr, "4. %s: Array size 500, add_three\n", result != 1 ? "FAILED" : "PASSED");

    map_char(subtract_three, test_source_4, test_dest_4, 500);
    result = chars_are_equal(subtract_three, test_source_4, test_dest_4, 500);
    fprintf(stderr, "4. %s: Array size 500, subtract_three\n", result != 1 ? "FAILED" : "PASSED");

    map_char(multiply_by_three, test_source_4, test_dest_4, 500);
    result = chars_are_equal(multiply_by_three, test_source_4, test_dest_4, 500);
    fprintf(stderr, "4. %s: Array size 500, multiply_by_three\n", result != 1 ? "FAILED" : "PASSED");

    map_char(divide_by_three, test_source_4, test_dest_4, 500);
    result = chars_are_equal(divide_by_three, test_source_4, test_dest_4, 500);
    fprintf(stderr, "4. %s: Array size 500, divide_by_three\n", result != 1 ? "FAILED" : "PASSED");

    fprintf(stderr, "\n");

}

void test_map_float()
{
    fprintf(stderr, "------------------------ TEST: map_float() -----------------------\n");

    // 1. Array size 0
    float test_source_1[0];
    float test_dest_1[0];

    int result = map_float(add_four, test_source_1, test_dest_1, 0);
    fprintf(stderr, "1. %s: Array size 0, add_four\n", result != -1 ? "FAILED" : "PASSED");

    result = map_float(subtract_four, test_source_1, test_dest_1, 0);
    fprintf(stderr, "1. %s: Array size 0, subtract_four\n", result != -1 ? "FAILED" : "PASSED");

    result = map_float(multiply_by_four, test_source_1, test_dest_1, 0);
    fprintf(stderr, "1. %s: Array size 0, multiply_by_four\n", result != -1 ? "FAILED" : "PASSED");

    result = map_float(divide_by_four, test_source_1, test_dest_1, 0);
    fprintf(stderr, "1. %s: Array size 0, divide_by_four\n", result != -1 ? "FAILED" : "PASSED");

    // 2. Array size 1
    float test_source_2[1] = {(float)rand()};
    float test_dest_2[1];

    map_float(add_four, test_source_2, test_dest_2, 1);
    result = floats_are_equal(add_four, test_source_2, test_dest_2, 1);
    fprintf(stderr, "2. %s: Array size 1, add_four\n", result != 1 ? "FAILED" : "PASSED");

    map_float(subtract_four, test_source_2, test_dest_2, 1);
    result = floats_are_equal(subtract_four, test_source_2, test_dest_2, 1);
    fprintf(stderr, "2. %s: Array size 1, subtract_four\n", result != 1 ? "FAILED" : "PASSED");

    map_float(multiply_by_four, test_source_2, test_dest_2, 1);
    result = floats_are_equal(multiply_by_four, test_source_2, test_dest_2, 1);
    fprintf(stderr, "2. %s: Array size 1, multiply_by_four\n", result != 1 ? "FAILED" : "PASSED");

    map_float(divide_by_four, test_source_2, test_dest_2, 1);
    result = floats_are_equal(divide_by_four, test_source_2, test_dest_2, 1);
    fprintf(stderr, "2. %s: Array size 1, divide_by_four\n", result != 1 ? "FAILED" : "PASSED");

    // 3. Array size 2
    float test_source_3[2] = {(float)rand(), (float)rand()};
    float test_dest_3[2];

    map_float(add_four, test_source_3, test_dest_3, 2);
    result = floats_are_equal(add_four, test_source_3, test_dest_3, 2);
    fprintf(stderr, "3. %s: Array size 2, add_four\n", result != 1 ? "FAILED" : "PASSED");

    map_float(subtract_four, test_source_3, test_dest_3, 2);
    result = floats_are_equal(subtract_four, test_source_3, test_dest_3, 2);
    fprintf(stderr, "3. %s: Array size 2, subtract_four\n", result != 1 ? "FAILED" : "PASSED");

    map_float(multiply_by_four, test_source_3, test_dest_3, 2);
    result = floats_are_equal(multiply_by_four, test_source_3, test_dest_3, 2);
    fprintf(stderr, "3. %s: Array size 2, multiply_by_four\n", result != 1 ? "FAILED" : "PASSED");

    map_float(divide_by_four, test_source_3, test_dest_3, 2);
    result = floats_are_equal(divide_by_four, test_source_3, test_dest_3, 2);
    fprintf(stderr, "3. %s: Array size 2, divide_by_four\n", result != 1 ? "FAILED" : "PASSED");

    // 4. Array size 500
    float test_source_4[500];
    for (int i = 0; i < 500; ++i)
        test_source_4[i] = (float)rand();
    float test_dest_4[500];

    map_float(add_four, test_source_4, test_dest_4, 500);
    result = floats_are_equal(add_four, test_source_4, test_dest_4, 500);
    fprintf(stderr, "4. %s: Array size 500, add_four\n", result != 1 ? "FAILED" : "PASSED");

    map_float(subtract_four, test_source_4, test_dest_4, 500);
    result = floats_are_equal(subtract_four, test_source_4, test_dest_4, 500);
    fprintf(stderr, "4. %s: Array size 500, subtract_four\n", result != 1 ? "FAILED" : "PASSED");

    map_float(multiply_by_four, test_source_4, test_dest_4, 500);
    result = floats_are_equal(multiply_by_four, test_source_4, test_dest_4, 500);
    fprintf(stderr, "4. %s: Array size 500, multiply_by_four\n", result != 1 ? "FAILED" : "PASSED");

    map_float(divide_by_four, test_source_4, test_dest_4, 500);
    result = floats_are_equal(divide_by_four, test_source_4, test_dest_4, 500);
    fprintf(stderr, "4. %s: Array size 500, divide_by_four\n", result != 1 ? "FAILED" : "PASSED");

    fprintf(stderr, "\n");

}

int main()
{
    time_t current_time;
    srand((unsigned) time(&current_time));

    test_map_int();
    test_map_char();
    test_map_float();

    return 0;
}