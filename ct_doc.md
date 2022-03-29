{% include navigation.html %}

# Katie's Create Task Outline
### Idea: RGB Student Art Feature
_Description:_ Student art with data (RGB, Hex Code, and Binary), grayscale, which dynamically changes RGB values, and pinkscale features.
<br>


## [Overview of the CB "Create Performance Task"](https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf?course=ap-computer-science-principles)
- Final program code (created independently or collaboratively)  
- A video that displays the running of your program and demonstrates functionality you developed (created independently) 
- Written responses to all the prompts in the performance task (created independently)

## _Final Program Code Requirements:_
- Instructions for input from one of the following:
- - the user (including user actions that trigger events)
- - **Example:** in [rgb.html](https://github.com/Tyler929/WalkieTalkies/blob/main/templates/rgb.html) (button that toggles grayscale and regular image by user input)
```
img class="img-responsive py-3" id=img{{loop.index}} alt="" width="256" height="Auto" src="{{image.base64}}">
                            <p hidden id="img_orig{{loop.index}}">{{image.base64}}</p>
                            <button onclick="toggle()">Grayscale!</button>
```
```
<p hidden id="img_pink{{loop.index}}">{{image.base64_PINK}}</p>
                            <button id="pinkbutton{{loop.index}}" onclick="pinkScale({{loop.index}})">Pinkscale!</button>
```
```
<p hidden id="img_gray{{loop.index}}">{{image.base64_GRAY}}</p>
                            <button onclick="toggle()">Back to original :)</button>
```

<br>

- Use of at least one list (or other collection type) to represent a collection of
data that is stored and used to manage program complexity and help fulfill
the program’s purpose
- - **Example:** in [image.py](https://github.com/Tyler929/WalkieTalkies/blob/main/image.py)
```
def image_data(path=Path("static/rgb/"), img_list=None):  # info: path of static images is defaulted
    if img_list is None:  # info: color_dict is defined with defaults and these are the images showing up
        img_list = [
            {'source': "Ceramics 2", 'label': "Katie Hickman", 'file': "katiergbbb.jpeg"},
        ]
```
<br>

- At least one procedure that contributes to the program’s intended purpose,
where you have defined:
- - the procedure’s name
- - the return type (if necessary)
- - one or more parameters 
- - **Example:**
```
 function pinkScale(index) {
            if (document.getElementById("pinkbutton" + index).innerText == "Pinkscale!") {
                document.getElementById("img" + index).src = document.getElementById("img_pink" + index).innerText;
                document.getElementById("pinkbutton" + index).innerText = "Back to Original :)";
            }
            else
            {
                document.getElementById("img" + index).src = document.getElementById("img_orig" + index).innerText;
                document.getElementById("pinkbutton" + index).innerText = "Pinkscale!";
            }
        }
```
```
var imageType = 2;
        function toggle() {
            if (imageType == 2) {
                $('#colorscale').hide()
                $('#grayscale').show()
                imageType = 1; <!-- allows for toggling back and forth -->
            } else {
                $('#grayscale').hide()
                $('#colorscale').show()
                imageType = 2; <!-- allows for toggling back and forth -->
            }
        }
```
<br>

- An algorithm that includes sequencing, selection, and iteration that is in the
body of the selected procedure
- - **Example:**
```
 img_dict['hex_array_GRAY'] = []
        img_dict['binary_array_GRAY'] = []
        # for grayscale binary/hex changes
        for pixel in img_dict['gray_data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            img_dict['hex_array_GRAY'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            img_dict['binary_array_GRAY'].append(bin_value)
```
<br>

- Calls to your student-developed procedure
- - **Example:**
```
img class="img-responsive py-3" id=img{{loop.index}} alt="" width="256" height="Auto" src="{{image.base64}}">
                            <p hidden id="img_orig{{loop.index}}">{{image.base64}}</p>
                            <button onclick="toggle()">Grayscale!</button>
```

### [Full rgb.html File Code](https://github.com/Tyler929/WalkieTalkies/blob/main/templates/rgb.html)

### [Full image.py File Code](https://github.com/Tyler929/WalkieTalkies/blob/main/image.py)

### App Route in [main.py](https://github.com/Tyler929/WalkieTalkies/blob/main/main.py) Code:
```
@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    path = Path(app.root_path) / "static" / "rgb"
    return render_template('rgb.html', images=image_data(path))
```

<br>
<br>

## _Video Requirements_: [Link to my video](https://drive.google.com/file/d/10-9cMdOrcTTSnl8QF2g4XYbiwbBXHSur/view?usp=sharing)
Submit one video file that demonstrates the running of your program as
described below. Collaboration is not allowed during the development of
your video.
- Your video must demonstrate your program running, including:
- - Input to your program
- - At least one aspect of the functionality of your program
- - Output produced by your program
- Your video may NOT contain:
- - Any distinguishing information about yourself
- - Voice narration (though text captions are encouraged)
- Your video must be:
- - Either .mp4, .wmv, .avi, or .mov format **(.mov)**
- - No more than 1 minute in length **(59 seconds)**
- - No more than 30MB in file size **(3.8MB)**

<br>
<br>

## _Written Responses_:
Submit your responses to prompts 3a – 3d, which are described below. Your
response to all prompts combined **must not exceed 750 words** (program code
is not included in the word count). Collaboration is not allowed on the written
responses. Instructions for submitting your written responses are available on
the AP Computer Science Principles Exam Page on AP Central.

**Total word count: 506**

**3 a.** Provide a written response that does all three of the following:
_Approx. 150 words (for all subparts of 3a combined)_ 

**i.** Describes the overall purpose of the program

The purpose of my program is to extract RGB, Hex Code, and Binary values from pixels in an image, and then change these pixels into grayscale and pink-scale. My program also displays metadata for the image from a list and has two buttons for the grayscale and pink-scale operations.

**ii.** Describes what functionality of the program is demonstrated in
the video

In my video, the user pushes the grayscale button and the image turns gray, along with the data values changing to pertain to the new gray image. The user pushes the button, that now says "back to original". The images reverts to normal and the data values follow. Next, the user pushes the pinkscale button and the image turns pink. 

**iii.** Describes the input and output of the program demonstrated in
the video

In my video, the input is the user pushing the grayscale and pink-scale buttons. The output is the image toggling from normal to gray and from normal to pink when their respective buttons are pressed.

**3 b.** Capture and paste two program code segments you developed during
the administration of this task that contain a list (or other collection
type) being used to manage complexity in your program.
_Approx. 200 words (for all subparts of 3b combined, exclusive of program code)_

**i.** The first program code segment must show how data have been
stored in the list.

```
def image_data(path=Path("static/rgb/"), img_list=None):  # info: path of static images is defaulted
    if img_list is None:  # info: color_dict is defined with defaults and these are the images showing up
        img_list = [
            {'source': "Ceramics 2", 'label': "Katie Hickman", 'file': "katiergbbb.jpeg"},
        ]
```

**ii.** The second program code segment must show the data in the
same list being used, such as creating new data from the existing
data or accessing multiple elements in the list, as part of fulfilling
the program’s purpose.

```
for img_dict in img_list:
        # to fix static images
        file = path / img_dict['file']
        print(file)

        img_reference = Image.open(file)
        img_data = img_reference.getdata()  # https://www.geeksforgeeks.org/python-pil-image-getdata/
        img_dict['format'] = img_reference.format
        img_dict['mode'] = img_reference.mode
        img_dict['size'] = img_reference.size

        # info: Conversion of original Image to Base64, a string format that serves HTML nicely
        img_dict['base64'] = image_formatter(img_reference, img_dict['format'])

        # info: Numpy is used to allow easy access to data of image, python list
        img_dict['data'] = numpy.array(img_data)
        img_dict['hex_array'] = []
        img_dict['binary_array'] = []
        # grayscale
        img_dict['gray_data'] = []
        # pinkscale
        img_dict['pink_data'] = []
```

Then, provide a written response that does all three of the following:

**iii.** Identifies the name of the list being used in this response

Name: img_list

**iv.** Describes what the data contained in the list represent in your
program

The data in my list represents the image file, which is called "Student Image" when displayed on the webpage and "katiergbbb.jpeg" in the list. It also contains the source and label, which is metadata. 

**v.** Explains how the selected list manages complexity in your program
code by explaining why your program code could not be written, or
how it would be written differently, if you did not use the list

The selected list manages complexity in my program by preventing rewriting the same code segment for each image in the list. If I did not use the list, my code would be repetitive and would not be as efficient as if I had used my list. 

**3 c.** Capture and paste two program code segments you developed during
the administration of this task that contain a student-developed
procedure that implements an algorithm used in your program and a
call to that procedure.
_Approx. 200 words (for all subparts of 3c combined, exclusive of program code)_

**i.** The first program code segment must be a student-developed
procedure that:
- Defines the procedure’s name and return type (if necessary)
- Contains and uses one or more parameters that have an effect
on the functionality of the procedure
- Implements an algorithm that includes sequencing, selection,
and iteration

```
       function pinkScale(index) {
            if (document.getElementById("pinkbutton" + index).innerText == "Pinkscale!") {
                document.getElementById("img" + index).src = document.getElementById("img_pink" + index).innerText;
                document.getElementById("pinkbutton" + index).innerText = "Back to Original :)";
            }
            else
            {
                document.getElementById("img" + index).src = document.getElementById("img_orig" + index).innerText;
                document.getElementById("pinkbutton" + index).innerText = "Pinkscale!";
            }
        }


average = (pixel[0] + pixel[1] + pixel[2]) // 3
            if len(pixel) > 3:
                # grayscale
                img_dict['gray_data'].append((average, average, average, pixel[3]))
                # pinkscale
                img_dict['pink_data'].append((average, 0, average, pixel[3]))
            else:
                # grayscale
                img_dict['gray_data'].append((average, average, average))
                # pinkscale
                img_dict['pink_data'].append((average, 0, average))
```

**ii.** The second program code segment must show where your
student-developed procedure is being called in your program.

```
 <p hidden id="img_pink{{loop.index}}">{{image.base64_PINK}}</p>
 <button id="pinkbutton{{loop.index}}" onclick="pinkScale({{loop.index}})">Pinkscale!</button>
```

Then, provide a written response that does both of the following:

**iii.** Describes in general what the identified procedure does and how it
contributes to the overall functionality of the program

In general, the procedure contributes to the overall function of the program because this procedure is the pink-scale function, which is needed to change the pixels in the image from original to pink. The procedure works with the backend python code in image.py to average the red and blue values in a pixel. 

**iv.** Explains in detailed steps how the algorithm implemented in the
identified procedure works. Your explanation must be detailed
enough for someone else to recreate it.

First, the procedure appears as "Pinkscale!". The user clicks on the button, and the text on the button is changed to "Back to Original!". The  red and blue values in the pixels are averaged, which means totaled and divided by 3. This looks like the following in RGB format: (average, 0, average). Then, the user clicks on the button that now reads "Back to Original!" and the image returns to its regular RGB values. 

**3 d.** Provide a written response that does all three of the following:
_Approx. 200 words (for all subparts of 3d combined)_

**i.** Describes two calls to the procedure identified in written response
3c. Each call must pass a different argument(s) that causes a
different segment of code in the algorithm to execute.

_First call:_

The first call occurs when the user first presses the "Pinkscale!" button. The <button id="pinkbutton{{loop.index}}" onclick="pinkScale({{loop.index}})"> calls the procedure to average the pixels in the original image to make them appear pink. 

_Second call:_

The second call occurs when the user presses the button once more to return the image back to normal. After being clicked once already, the button will read "Back to Original :)". When the user clicks it, the image will revert to normal and the button will read "Pinkscale!" once again. 


**ii.** Describes what condition(s) is being tested by each call to the
procedure

_Condition(s) tested by the first call:_

If the button is clicked and the image is in its original form, the images' pixels will be averaged to appear pink. 


_Condition(s) tested by the second call:_

If the button is clicked and the image is in its pink-scale form, the images' pixels will return to normal and look regular once again. 



**iii.** Identifies the result of each call

_Result of the first call:_

The result of the first call is the pixels in the images averaging to pink. The image appears pink now.


_Result of the second call:_

The result of the second call is the pixels returning to normal. The image appears normal now. 
