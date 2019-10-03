

  let images =[
    "ASSETS/images_(1).png",//insert here the url you can add more items
    "ASSETS/images_(2).png",//insert here the url you can add more items
    "ASSETS/images_(3).png",//insert here the url you can add more items
    "ASSETS/images_(4).png",//insert here the url you can add more items
    "ASSETS/images.png",//insert here the url you can add more items
    "ASSETS/vitamin-icon-2.jpg"//insert here the url you can add more items
    /*copy and paste to add more*/
  ]

  let i = 0
  let src = ""

  function refresh(){
    document.querySelector("img").setAttribute("src", src)
    document.querySelector("#result").innerHTML = output
  }

  let fig = document.createElement("figure");// you can change html element here
  fig.setAttribute("id","mysvg")
  document.body.appendChild(fig)
  let img = document.createElement("IMG")
  img.setAttribute("width", "50") /* set desired item size otherwise full-size*/
  img.setAttribute("heigh", "50")//* set desired item sizeotherwise full-size*/
  fig.appendChild(img);
  let range_slider = document.querySelector("input[type=range]")
  range_slider.min = 1;
  range_slider.max = range_slider.value = images.length -1
  range_slider.step =range_slider.getAttribute("step") ;
  let input = document.querySelector("#result")
  let output = i + 1
  input.innerHTML = output


  document.addEventListener( 'DOMContentLoaded', (event) => {
    refresh()
    randomElement = false;//set to false to stop random
      if (randomElement == true) {
        document.querySelector("input[type=range]").addEventListener('input', (event) => {
        let val= range_slider.value
          output = val
         let randomElement = images [Math.floor(Math.random() * images.length) ]
          for( i = 0; i < randomElement.length; i++){
            i
            refresh()
            src = randomElement
          }
        })
      }else{
        document.querySelector("input[type=range]").addEventListener('input', (event) => {
          let value = range_slider.value
          console.log(value)
          output= value
          src=images[value]
        })
      }
  });
