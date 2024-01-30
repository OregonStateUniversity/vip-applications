package main

func Map[input_type any, output_type any](
	input_slice []input_type,
	trasnformation_func func(input_type) output_type,
) []output_type {

	result_slice := make([]output_type, len(input_slice))

	return result_slice
}
