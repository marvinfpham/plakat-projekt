# Plakat Projekt

A Danish poster commerce project. The current implementation is an **unpublished Shopify Online Store 2.0 theme** based on [Dawn 16.0.0](https://github.com/Shopify/dawn/tree/v16.0.0), with an original editorial homepage section and Danish working copy. The identity and artwork are provisional. A live store, products, fulfillment and automation are not connected.

## Local development

Requirements: Node 24+, npm 11+, Python 3.12+. From this repository root:

```sh
npm ci
npm run theme:check
npm run theme:package
python -m unittest discover -s tests -v
```

With an authorized Shopify development store, log in through Shopify CLI and use `npm run theme:dev -- --store YOUR-STORE.myshopify.com`. This uploads a development theme for preview; do not publish it without owner approval. The generated ZIP is ignored by Git. Set the store's primary language to Danish in Shopify before reviewing Danish customer journeys.

## Economics

`python tools/unit_economics.py path/to/quote.json` computes contribution from entered figures. The JSON needs `price_incl_vat` and `vat_rate`; optional fields are `production_ex_vat`, `shipping_ex_vat`, `payment_fees`, `replacement_reserve`, `marketing_cost` and `automation_cost`. Identify whether each input is a quote, actual or estimate. Tax and accounting treatment requires professional review.

## Project state

Read [the Stage A plan](docs/research/STAGE_A.md), [status](CURRENT_STATUS.md) and [backlog](BACKLOG.md). Shopify Dawn's license is included at [theme/LICENSE.md](theme/LICENSE.md); use this theme only with Shopify.
