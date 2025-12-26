# Data Generation 
Purpose of this data
- This project does not use real client data. Instead, we generate synthetic business data that behaves like real retail data.

Intutive Logic we have used:
- prices affect sales,
- discounts boost demand,
- marketing helps but with limits,
- sales vary across stores, products, and time.

This allows us to: test data cleaning logic, build demand models, run pricing and discount simulations,


Time and business structure

- Time unit: 1 week
- Total duration: 52 weeks

Business units:

- 10 stores
- 50 products

Each product belongs to one category, Each row in the raw sales data represents:One product sold in one store during one week

Tables generated

We generate four raw tables, similar to what a client would provide.

1. Product table (product.csv)

Contains fixed information about products.

Columns:
- product_id: unique product code
- category: type of product (e.g. Snacks, Dairy)
- cost_price: cost to the business

Logic used

Cost prices are mostly reasonable, with a few expensive products.

This is done using a skewed distribution so that:

most products are affordable,

some products are premium.

2. Sales table (sales.csv)

Contains weekly sales activity.

Columns:

- week
- store_id
- product_id
- units_sold
- selling_price

This is the main table used later for modeling.

3. Discount table (discount.csv)

Contains promotional discounts.

Columns:

- week
- store_id
- product_id
- discount_percent

Important:

Discounts are not present for every product every week. Some categories receive discounts more often than others.

Some discount records are missing on purpose (to simulate real data gaps).

4. Marketing table (marketing.csv)

Contains store-level marketing spend.

Columns:

- week
- store_id
- marketing_spend

Logic used

Marketing spend:

varies by store,

increases during peak demand weeks,

contains random noise.

--- 

### How selling price is generated

Each product has a base price:

```
base price = cost price × margin factor
```


Where:

margin factor varies across products,

prices fluctuate slightly week to week to simulate real pricing changes.

Final selling price is:
```
selling price = base price × small random change
```

This creates:

small weekly price movements,

no unrealistic price jumps.

How demand (units sold) is generated

Units sold are calculated using simple, explainable building blocks.

1. Step 1: Base demand

Each product has a base popularity level.

Some products sell more naturally than others.

base demand = product-specific value

2. Step 2: Store effect

Some stores perform better than others.

store effect = multiplier between 0.75 and 1.35


This reflects:

footfall differences,

location strength.

3. Step 3: Seasonality

Demand increases during certain weeks (e.g. festive period).

We apply a smooth seasonal increase around peak weeks.

seasonality factor > 1 during peak weeks

4. Step 4: Discount effect

Higher discounts increase demand.

discount boost = 1 + (discount percent × 0.03)


Interpretation:

every 1% discount increases demand by ~3% (on average),

this is an assumption, not a claim.

5. Step 5: Price sensitivity

Demand decreases when price increases.

We use a price sensitivity factor that varies by category.
```
price effect = (discounted price / base price) ^ (−price sensitivity)
```

Interpretation:

if price goes up, demand goes down,

snacks and beverages are more sensitive than staples.

6. Step 6: Marketing effect

Marketing increases demand, but with diminishing returns.
```
marketing effect = 1 + 0.30 × scaled log(marketing spend)
```

This ensures:

marketing helps,

doubling spend does not double demand.

7. Step 7: Random noise

Finally, random variation is added.

final units sold = all effects × random noise


This avoids:

perfectly smooth data,

unrealistic predictability.

Intentional data issues (very important)


