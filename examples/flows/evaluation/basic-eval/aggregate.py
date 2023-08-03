from typing import List

from promptflow import tool


@tool
def aggregate(processed_results: List[str], variant_ids: List[str], line_numbers: List[int]):
    """
    This tool aggregates the processed result of all lines to the variant level and log metric for each variant.

    :param processed_results: List of the output of line_process node.
    :param variant_ids: List of variant ids that can be used to group the results by variant.
    :param line_numbers: List of line numbers of the variants. If provided, this can be used to
                        group the results by line number.
    """

    # Add your aggregation logic here
    # aggregated_results should be a dictionary with variant id as key, and for each variant id, it is also a
    # dictionary with the metric name as the key and the metric value as the value.
    # For example: {
    #    "variant_0": {
    #       "metric_name_0": metric_value_0,
    #       "metric_name_1": metric_value_1,
    #       ...
    #    },
    #    "variant_1": {
    #       ...
    #    },
    #    ...
    # }
    aggregated_results = {}

    # Log metric for each variant
    # from promptflow import log_metric
    # log_metric(key="<my-metric-name>", value=aggregated_results["<variant-id>"]["<my-metric-name>"],
    #            variant_id="<variant-id>")

    return aggregated_results
