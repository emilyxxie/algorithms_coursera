def max_ad_rev(ads, pay_click, avg_clicks):
  pp_click.sort(reverse = True)
  avg_clicks.sort(reverse = True)
  return sum(
    [x * y for x, y in zip(pp_click, avg_clicks)]
  )

# pay per click
ads = 3
pp_click = [1, 3, 5]
avg_clicks = [2, 4, 1]

print(max_ad_rev(ads, pp_click, avg_clicks))
