# Stage A: Danish poster business audit and proposed architecture

Date: 2026-10-09. Status: proposed, awaiting owner approval. This is a decision document, not evidence of a launched business.

## Objective and evidence limits

Build a premium, original Danish poster business with low fixed costs and repeatable operations. The owner's role is to approve creative work, financial commitments and production changes, and review performance. Profitability is a hypothesis to test, not an outcome established by this audit.

Verified in this environment: the selected `marvinfpham/plakat-projekt` checkout is a valid, clean, unborn Git repository, and `git ls-remote origin HEAD` succeeds but returns zero refs. Git, Node 24, npm 11, Python 3.12, Codex CLI 0.159.0-alpha.3 and GitHub CLI are present. Codex can edit local files and access the approved GitHub proxy. This task runs on a cloud machine, independently of the owner's laptop while it is active. Available cloud environment draft tools can save setup/start instructions, but that is not a business scheduler. No Shopify, POD, analytics or accounting credential was found by name. A GH_TOKEN variable exists by name; its value and capabilities were not inspected. No account creation, store access, background scheduling or external API operation was verified.

Direct access to `developers.openai.com` returned HTTP 403 through the current egress policy. Other vendor sites and live market listings were not verifiable in this run. OpenAI's [Codex source README](https://github.com/openai/codex) and Shopify's [Dawn README](https://github.com/Shopify/dawn) were retrieved. Links below are authoritative starting points, but claims relying on pages not retrieved here require rechecking before execution. Competitor prices, search demand, supplier quotes, product quality, current subscriptions and terms are unknown. No numerical market demand is asserted.

## Commercial assessment and collection hypotheses

A broad catalog of AI-like art would compete on price with established poster sellers. The initial advantage should be a coherent, original design voice, visible print quality, useful room styling and dependable EU delivery. POD avoids inventory but can compress margin and gives less control over color, paper and damage handling. Order samples before claiming premium quality.

| Hypothesis | Rationale | Risk | Validation before scale |
| --- | --- | --- | --- |
| Danish place and neighborhood series | Local gift and identity intent; room for original graphic treatment | Crowded city-print category; place names do not establish demand | Compare actual Danish SERPs, listings, price bands and search intent; test 3–5 motifs |
| Original typography/graphic statements in Danish | Distinct language and brand voice; can be rendered reliably | Trademark/copyright claims and low differentiation for slogans | Rights review, competitor sweep and small design tests |
| Nature/botanical with Nordic editorial style | Broad decor fit and natural collection coherence | Very crowded and weak specificity | Seek a distinctive visual system and compare conversion with place series |
| Personalized posters | High intent and differentiated gifting | Preview, error handling and returns complexity | Defer until basic order and fulfillment flow works |
| Children's rooms | Gift potential | Safety, taste, audience and rights sensitivity | Defer until brand and imagery rights are proven |

Recommendation: test two collections with 3–5 designs each, rather than produce 30 before evidence. Choose exact collections only after a documented Danish competitor/keyword scan and design review. For each candidate, capture dated competitor URL, size, price, shipping, material, visual positioning and actual search evidence from approved sources. Then use a limited storefront or prelaunch feedback round; no invented sales or search volumes.

## Architecture choices

| Decision | Proposed approach and why | Credible alternative / tradeoff | Cost and technical risk | Evidence |
| --- | --- | --- | --- | --- |
| Storefront | Shopify Online Store 2.0 theme, derived from a stable Dawn release, with native checkout. Lower operational burden and built-in commerce primitives. | Headless Shopify offers deeper UI control but adds hosting, API, SEO and checkout integration work. WooCommerce fits the owner's experience and allows hosting control, but adds plugin, security and update operations. | Shopify recurring fee and apps require current quotes. Theme customization can constrain complex personalization. | [Dawn](https://github.com/Shopify/dawn), [Shopify themes](https://shopify.dev/docs/storefronts/themes), [WooCommerce docs](https://woocommerce.com/documentation/) |
| Fulfillment | Pilot Gelato through its supported Shopify integration; manually reconcile first sample orders. | Printful or Printify may offer better specific SKU, quality, price or shipping. | Real SKU quotes, delivery SLAs, API rights and return terms unverified. No automated order writes until testing. | [Gelato developer docs](https://dashboard.gelato.com/docs/), [Printful API](https://developers.printful.com/docs/), [Printify API](https://developers.printify.com/) |
| AI work | Codex sessions for research, code and drafting, with scoped human review. Model nine requested responsibilities as checklists/workflows, not nine persistent agents. | A bespoke always-on multi-agent service adds complexity and token cost without validated demand. | Codex quotas, unattended invocation and API billing must be verified. | [Codex source](https://github.com/openai/codex), [Codex docs](https://developers.openai.com/codex/) |
| Operations state | Start with Shopify as source of truth for products/orders and GitHub Issues/PRs for development work; use a small durable job database only once automated external writes exist. | A full queue/dashboard now gives more control but creates hosting, security and recovery obligations. | Avoid duplicate order processing; add idempotency keys, webhook signature checks, retries and dead-letter state before unattended fulfillment. | [Shopify Admin API](https://shopify.dev/docs/api/admin-graphql), [Shopify webhooks](https://shopify.dev/docs/apps/build/webhooks) |
| Scheduling | Evaluate Codex native automation and supported cloud task APIs first; for deterministic checks use GitHub Actions schedule or managed worker if authorized. | A self-hosted always-on process can control timing but requires uptime, secrets, monitoring and cost. | Cloud Codex sessions do not prove 24/7 recurring execution. GitHub Actions schedules can be delayed and are not a durable order queue. | [GitHub scheduled events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule), [Codex docs](https://developers.openai.com/codex/) |
| Approval surface | Start with versioned design reviews and explicit Shopify draft/publish gate; build a small internal UI only after real workflow pain. | A bespoke approval center from day one improves centralization but delays commercial validation. | Approval must bind asset version, action, approver, time, scope and cost. | [Shopify products](https://shopify.dev/docs/api/admin-graphql), [GitHub reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests) |

OpenAI dots are not verified here. Do not depend on them or equate them with Codex. The Codex CLI and this session are verified; desktop app, SDK, scheduled cloud tasks, independent subagent scheduling and dots provisioning need capability and account checks. Being able to spawn an agent in a live session would not establish persistent agents. The laptop can be off during a hosted task, but true unattended operations require a separately deployed scheduler/worker, durable state, authenticated integrations, alerts, bounded budgets and recovery tests.

## Unit economics and spending gate

Keep actuals, quoted costs and illustrative numbers separate. Illustrative 30×40 cm unframed poster at DKK 299 including assumed 25% VAT: net sales DKK 239.20. If production is DKK 95, shipping DKK 45, payment/platform variable fees DKK 8 and returns/replacements reserve DKK 12, contribution is DKK 79.20 before fixed costs, marketing and AI. This is **not** a supplier quote or profit forecast. At hypothetical fixed monthly costs of DKK 500, break-even would be 7 such orders before owner labor and acquisition; at DKK 1,500, 19. Verify VAT treatment, shipping tax, fee schedules and real invoices with an accountant.

Proposed decision thresholds, subject to actual quotes: target at least 30% contribution on ex-VAT sales before paid acquisition; pause any SKU with negative realized contribution or repeated quality issues; cap new recurring commitments at DKK 0 until approved. Planning envelopes only: lean validation DKK 0–1,000/month plus approved samples; hosted automation and paid Shopify/apps may raise this to roughly DKK 1,000–3,000/month before advertising. These ranges are placeholders, not researched prices. Obtain current written quotes for Shopify, POD, domain, samples, email, accounting, worker and API usage. Proposed initial approved budget should be determined from those quotes, with a separate cap for samples and no advertising spend at launch.

## Required services, ownership and risk controls

After approval, use the existing repository, a Shopify development store, one POD account, a business domain, analytics/search accounts and Danish accounting/invoicing service selected with an accountant. Some of these may already exist. Check access first. Codex can create local project files and tests, configure a theme and CI, prepare draft products, build integrations and request read-only API operations when credentials permit. Store creation, paid plans, domain purchase, company/legal identity, payment onboarding, taxes, consent language, sample purchases and production publishing require the owner's account/decision and sometimes specialist review. Credentials belong in supported secret storage, never repository files. Do not touch Plomme or RecordsUp.

Risks: copyright/trademark and asset licenses; color/print defects; POD shipping/returns; GDPR and Danish consumer disclosures; price and VAT errors; duplicate fulfillment; account suspension from unsupported automation; quota exhaustion; insecure webhook handling. Mitigation: original source assets and license log, versioned proof approval, paid sample gate, legal/accounting review, signed webhooks, idempotent reconciliation, kill switch, least privilege, backups, audit log and spending caps. Never send production customer PII into a broad AI task by default.

## Prioritized execution after approval

1. M1: complete dated competitor/keyword and supplier SKU/quote matrix; verify official platform/API terms; ask owner to pick positioning and spending cap. Exit: defensible price and 2 collection briefs.
2. M3–M4: initialize existing repo; build a Shopify 2.0 theme with CI and development store, then smoke test native browsing/cart/checkout in a permitted test flow. Exit: usable unpublished storefront.
3. M5: design 6–10 versioned originals, validate fonts/assets and print specs, obtain version-specific approval, order approved samples. Exit: accepted print quality.
4. M6–M7: draft catalog, real margin calculator, POD mapping and test orders; add a minimal audit/approval record before write automation. Exit: end-to-end fulfillment and recovery test with no duplicate orders.
5. M8–M10: SEO, Merchant eligibility, analytics, consent, monitoring, privacy/security review and accounting reconciliation. Add scheduled deterministic jobs only where needed. Exit: measured operation and tested incident response.
6. M11–M12: owner-approved controlled launch, measure conversion and realized contribution, then decide whether personalization, more collections or a custom operations dashboard pay for themselves.

The production queue/dashboard and nine independent agents are removed from the MVP. Add a database-backed job system only for proven recurring workflows; states should include proposed, approved, queued, running with lease, retrying, blocked, awaiting review, completed and cancelled. Require bounded retry, dead-letter handling, idempotency, alerting and stop control before unattended writes. Future business reuse should come from small reusable modules, not a multi-tenant platform now.

## Approval boundary

Approval requested: proceed with the staged architecture above using the current repository and a Shopify 2.0 theme, validate two small collections, begin with supervised POD operations, and defer bespoke dashboard and persistent agent infrastructure until needed. This does **not** authorize new paid subscriptions, sample orders, public launch, live advertising, production publishing or use of unrelated projects. Those require specific later approvals with concrete cost and action.
