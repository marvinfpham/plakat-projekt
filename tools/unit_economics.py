"""Calculate per-order contribution from entered, ex-VAT supplier costs.

This is a planning aid, not tax or accounting software. All amounts are DKK.
"""
import argparse
import json
from decimal import Decimal, InvalidOperation


def nonnegative(value):
    try:
        amount = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError(f"invalid amount: {value}") from exc
    if not amount.is_finite() or amount < 0:
        raise ValueError(f"amount must be finite and nonnegative: {value}")
    return amount


def contribution(inputs):
    price = nonnegative(inputs["price_incl_vat"])
    vat_rate = nonnegative(inputs["vat_rate"])
    if vat_rate > 1:
        raise ValueError("vat_rate must be a fraction between 0 and 1")
    net_sales = price / (1 + vat_rate)
    cost_keys = ("production_ex_vat", "shipping_ex_vat", "payment_fees", "replacement_reserve", "marketing_cost", "automation_cost")
    costs = {key: nonnegative(inputs.get(key, 0)) for key in cost_keys}
    total_variable_cost = sum(costs.values(), Decimal(0))
    amount = net_sales - total_variable_cost
    return {
        "net_sales_ex_vat": round(net_sales, 2),
        "variable_costs_ex_vat": round(total_variable_cost, 2),
        "contribution_ex_vat": round(amount, 2),
        "contribution_margin_pct": round(100 * amount / net_sales, 2) if net_sales else None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("quote_json", help="JSON file with actual or explicitly labelled estimated inputs")
    args = parser.parse_args()
    with open(args.quote_json, encoding="utf-8") as source:
        data = json.load(source)
    print(json.dumps(contribution(data), indent=2, default=str))


if __name__ == "__main__":
    main()
