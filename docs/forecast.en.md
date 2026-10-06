# Forecast

!!! abstract "About this chapter"
    This chapter covers the Forecast. The forecast extracts things such as **the periods when an aspect forms** within a range you specify. The screen has three tabs: **Event Calculation / Time Map / Graphic Ephemeris**. The forecast is available on the **Plus plan and above** (Graphic Ephemeris = **Pro and above**, Time Map = **Max**).

## Event presets (the quick way)

![The Event Calculation tab (event preset, start date, period, transit location)](assets/forecast-01-preset.jpg)

### Steps

1. Choose the **birth data** you want to forecast in the birth data picker in the header.
2. Open **Forecast** from the menu.
3. Choose **Axis Transit**, **Success Aspects**, **Romance**, or **Major Events** from **Event Preset** (the calculation conditions are set automatically).
4. Enter the **Start Date**.
5. Specify the period (with the **7 days / 1 month / 1 year to 50 years** buttons, or freely with an **End Date**). When you press a button, the **End Date** field also changes to the start date plus that period.
6. Press **Calculate** and the matching periods are listed.

### Notes

- **Axis Transit**: narrows to the periods involving the ASC and MC.
- **Success Aspects**: targets the Sun, Jupiter, Pluto, and MC.
- **Romance**: narrows to the periods involving Venus.
- **Major Events**: targets the major bodies, and the result rows are color-coded. Colored rows contain the bodies most likely to manifest, with red leaning hard and blue leaning soft. Accurate interpretation still requires reading the individual natal chart.
- Choosing **None** clears the preset.
- The bodies used by the presets are not greatly affected by the transit location, so leaving it at the birth place is fine.

## Specifying detailed conditions yourself

![Specifying the calculation conditions (period type, target planets, aspects, period, transit location, advanced settings)](assets/forecast-02-conditions.jpg)

### Steps

1. Choose the **Period Type** (more than one can be selected). For example: **N-D (Solar Arc) / N-T (Transit) / N-P (Secondary) / P-P / P-T / D-T / T-T / T → House Ingress**.
2. Choose the bodies you want under **Target Planets** (with **All** and **None**).
3. Specify the aspect types you want and their **orbs** under **Aspect Settings**.
4. Set the **Start Date** and the **Transit Location** (**Search** looks up the latitude and longitude from a place name). There is also an **Orb** field next to the start date.
5. Opening **Advanced Settings** lets you include midpoint sensitive points and the midpoints of moving bodies.
6. Press **Calculate**.

### Notes

- There are two kinds of orb field.
    - The field next to each row of **Aspect Settings** (N-D, N-T, N-P, and so on) is an individual orb that applies **to that period type only**.
    - The **Orb** field next to the **Start Date** applies **to every period type**.
    - When both are filled in, **the individual orb wins**. When both are empty, the calculation uses the standard orbs.
- When the transiting **Moon** is included, the period is limited to a maximum of one month.
- Including fast-moving bodies over a long period produces a great many rows, so a warning message is shown.
- For the basics of aspects, see also [Aspects](https://www.arijp.com/basis/aspect) on the ARI official site (in Japanese).

## Reading the results

### Notes

- The columns of the **Aspect Formation Periods** list are **Natal / Aspect / Activator / Start / End / Exact** (the planets carry the prefixes N, D, T, and P).
- Clicking a date opens **the tri-wheel for that day** in a separate window.
    ![The tri-wheel for the day, opened by clicking a date](assets/forecast-03-result-triple.jpg)
- The **Print** button prints the list.

## Saving your conditions (events)

![Saving an event (the Save button, then giving the event a name)](assets/forecast-04-save-event.jpg)

### Steps

1. Once you have assembled your conditions, press **Save** and register them under an **Event Name**.
2. Recalling them from **Select event** restores the saved conditions.
3. After correcting recalled conditions, press **Overwrite**; when you no longer need them, press **Delete**.

## Time Map

The Time Map is available on the **Max plan**.

![The Time Map (the calculation results as horizontal bars on a timeline)](assets/forecast-05-timemap.jpg)

### Steps

1. Run **Event Calculation** first.
2. Open the **Time Map** tab and the results are laid out as horizontal bars (a Gantt chart) along a timeline.
3. **Print** prints it (A4 landscape).

### Notes

- House ingresses, such as "T → House Ingress", use arrows to show direct and retrograde motion.

## Graphic Ephemeris

This tab plots the motion of the bodies on a graph with time along the horizontal axis. The Graphic Ephemeris is available on the **Pro plan and above**.

![The Graphic Ephemeris input fields (birth data form, harmonic, Asp / All degrees, target planets, midpoints, period, transit location)](assets/forecast-06-gephemeris-form.jpg)

### Steps

1. Choose the birth data with the birth data picker in the header, then open the **Graphic Ephemeris** tab.
2. The **birth data form** at the top holds the selected person's date, time, and place of birth. It is the same form as on the Natal screen, and you can correct the values right here (see "Shifting the birth time to check it (rectification)" below).
3. Choose the **Harmonic** (H1(360) / H2(180) / H4(90) / H8(45) / H12(30) / Custom). With **H4**, for example, you can **spot 90-degree and 180-degree aspects as places where the lines cross**.
4. Ticking **Asp** shows aspect markers on the graph. Ticking **All degrees** next to it also shows the degrees of all bodies when you hover over the graph.
5. Choose the bodies for N (natal), D, P, and T under **Target Planets**.
6. Choosing planets under **Midpoint Lines** adds the **N/N midpoints** to the graph as well.
7. Set the **Start Date** and the period (or the end date), and the **Transit Location**. When you press a period button, the **End Date** field also changes to the start date plus that period.
8. Press **Draw** and the graph appears.

![The Graphic Ephemeris (horizontal lines for the natal bodies, lines for the moving bodies, planet symbols on the edges and at both ends of each line, and the crossings at the cursor)](assets/forecast-07-gephemeris-graph.jpg)

### Reading the graph

- The natal (N) bodies are drawn as horizontal dotted lines and the moving bodies (T, D, P) as lines. Where the lines cross, the aspect corresponding to the harmonic you chose is formed.
- The natal planet symbols are shown on the **left and right edges** of the graph. When planets are close in degree, their symbols are shifted slightly, with a thin line pointing to the actual position.
- Planet symbols also appear at **both ends** of each D, P, and T line: at the left and right edges of the graph, and also where a line **wraps at the top or bottom edge**. This makes it easy to follow lines that carry on across an edge, such as solar arc (D) lines.
- When you **hover over the graph**, the date is shown together with every line that is **within ±0.5°** of a natal line, with the aspect symbol and orb. Crossings closest to the cursor height are listed first and highlighted. For long periods, the date is shown as year and month (for example "2026.10").

### Shifting the birth time to check it (rectification)

You can shift the birth time step by step and check whether lines cross at the timing of past events.

1. Press **−10 min**, **−1 min**, **+1 min**, or **+10 min** next to **Birth time**, just above the graph. The graph redraws immediately. If you press the buttons several times in a row, the graph is redrawn once for the final time.
2. Keep shifting the time until the lines cross at the timing of the events.
3. Once you find the right time, save it with **Overwrite** in the birth data form. To keep the original and register the result as a separate record, press **Save As New**. **Shifting the time alone saves nothing.**

!!! tip "Collapse the inputs to see the graph larger"
    Pressing **Hide inputs** collapses the birth data form and the calculation settings together. The birth time buttons sit just above the graph, so you can keep using them with the inputs collapsed.

### Notes

- If you have edited the birth data form but have not pressed **Draw** yet, the graph on display is dimmed and a notice is shown. Pressing **Draw** redraws it from the current input.
- The **Print** button prints the graph on display. If you print with unsaved birth data, an **Unsaved birth data** badge appears in the heading.

!!! info "Plans"
    The Forecast page as a whole = **Plus and above**. Time Map = **Max and above** / Graphic Ephemeris = **Pro and above**.
