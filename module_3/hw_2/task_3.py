"""Задача 3
Метрики качества

Напишите функцию calculate_metrics(y_true, y_pred), которая принимает
на вход два списка y_true и y_pred, содержащих настоящие и предсказанные
значения бинарных классов (0 или 1 соответственно). Функция должна возвращать
словарь, содержащий значения метрик качества: accuracy, precision, recall"""


def calculate_metrics(y_true, y_pred):
    tp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 1)
    fp = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 1)
    fn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 1 and yp == 0)
    tn = sum(1 for yt, yp in zip(y_true, y_pred) if yt == 0 and yp == 0)

    accuracy = (tp + tn) / len(y_true) if len(y_true) > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0

    metrics = {"accuracy": accuracy, "precision": precision, "recall": recall}
    print(metrics)

    return metrics


def main():
    y_true = [0, 1, 1, 0, 1, 0]
    y_pred = [0, 1, 1, 0, 1, 0]
    calculate_metrics(y_true, y_pred)


if __name__ == "__main__":
    main()
