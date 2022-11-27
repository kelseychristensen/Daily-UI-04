<h1 align="center">Daily UI Day 04: Calculator</h1>

<p align="center">
This is a calculator for Daily UI's Day 04 challenge for the <a href="https://www.dailyui.co/"> 100 Days of UI 
challenge.</a></p>



## Links

- [Repo](https://github.com/kelseychristensen/Daily-UI-Day-04 "Daily UI Day 03 Repo")
- [Dribbble](https://dribbble.com/shots/19952876-Daily-UI-Day-04-Calculator "Dribbble Link")
- [Live Link](https://flooring-calculator.onrender.com "Live Link")

## Screenshots

![Calculator](/calc-1.PNG "Calculator")
![With Inputs](/calc-2.PNG "With Inputs")
![Result](/calc-3.PNG "Result")

### Built with

- HTML
- CSS
- Python
- Flask
- Bootstrap

### What went into this project

After setting up a very basic Flask server, I created the UI with HTML and CSS before using Python to ensure the calculator was completely functional.


### What I learned

I learned how to add a gradient overlay to an image. I've done gradients, and background images, but combining the two, even though it's simple enough, was a first for me. 


### Continued development

I think this project is simple, but fully realized. 

```html
{% if display_calc %}

<div class="card">
  <div class="card-body">
    <h6 class="card-subtitle mb-2 text-muted">You will need {{num_needed}} boxes of flooring.</h6>
    <p class="card-text">The total cost will be ${{calced_cost}}.</p>
  </div>
</div>
{% else %}

```
```css
.bg-image {
    background-image: linear-gradient(to left, rgb(224,225,222) 50%, rgb(224,225,222, 0)),
    url("/static/bernard-hermant-X-Bu9X6gok0-unsplash.jpg");
    height: 100%;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
```
## Author

Kelsey Christensen

- [Profile](https://github.com/kelseychristensen "Kelsey Christensen")
- [Email](mailto:kelsey.c.christensen@gmail.com?subject=Hi "Hi!")
- [Dribble](https://dribbble.com/kelseychristensen "Hi!")
- [Website](http://kelseychristensen.com/ "Welcome")
