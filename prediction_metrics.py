import math


def evaluate_predictions(actual, predicted):
    """Evaluate stock price predictions using MAE, RMSE, and MAPE."""

    if len(actual) != len(predicted):
        raise ValueError("Actual and predicted lists must have equal lengths.")

    if not actual:
        raise ValueError("Prediction lists cannot be empty.")

    errors = [abs(a - p) for a, p in zip(actual, predicted)]

    mae = sum(errors) / len(errors)

    rmse = math.sqrt(
        sum((a - p) ** 2 for a, p in zip(actual, predicted))
        / len(actual)
    )

    percentage_errors = [
        abs((a - p) / a) * 100
        for a, p in zip(actual, predicted)
        if a != 0
    ]

    mape = (
        sum(percentage_errors) / len(percentage_errors)
        if percentage_errors
        else None
    )

    return {
        "MAE": round(mae, 4),
        "RMSE": round(rmse, 4),
        "MAPE": round(mape, 2) if mape is not None else None,
    }


if __name__ == "__main__":
    actual_prices = [150, 155, 160, 158, 165]
    predicted_prices = [152, 153, 161, 157, 168]

    results = evaluate_predictions(actual_prices, predicted_prices)

    print("Stock Prediction Evaluation Results")
    for metric, value in results.items():
        print(f"{metric}: {value}")
