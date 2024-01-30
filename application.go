package TestMap

// Map Transform each element of input_slice
func Map[input_type any, output_type any](
	input_slice []input_type,
	trasnformation_func func(input_type) output_type,
) []output_type {

	result_slice := make([]output_type, len(input_slice))

	// Apply transformation_func to each input_slice element
	for index, value := range input_slice {
		result_slice[index] = trasnformation_func(value)
	}
	return result_slice
}
