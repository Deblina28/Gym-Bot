# Gym-Bot
A complete workout assistant

## Inspiration
Automating a task was our inspiration behind building this project. We first thought of making a simple hardware project that only counts the number of push-ups an individual performs. But later, we collaborated and thought of making a complete Murph workout assistant.

## What it does
Gym Bot is a workout assistant that reminds the user of doing a set of exercises. The hardware end of Gym Bot counts the number of push-ups being performed by the user. Gym Bot not only counts the number of push-ups in real-time and that too only if one performs the exercise correctly, but also automatically tweets about the number of push-ups one did that day. It is also installed with a timer and the Gym Bot assistant alarms one to switch to different types of exercises from time to time. And the moment the user starts exercising, the Gym Bot automatically plays music from a Youtube workout playlist. 

## How we built it
We used simple Infrared sensors to measure the proximity and set its threshold in such a way, that upon giving the pushups correctly, it will increment a counter. With that, we connected an OLED display for visualizing the no of pushups there. Both the IR sensor and the OLED display are driven by the Arduino. 
With that being said, our Hardware setup was complete.
Coming to the Software part we made a Python script, where we used Google's text to speech API for the assistant. It plays music along with the timer. And to read the no of pushups given by the user from Arduino, it uses pyserial for the serial communication and uses the counter value to speak the no. of pushups given.

## Challenges we ran into
The challenges we faced in building and setting up the hardware end of the project were that the LED for the proximity sensor wasn't working at first so we needed to replace that, and other than this troubleshooting and calibrating the sensor was a bit challenging.

The challenges faced while coding and setting up the software end were synching the voice assistant (tts using the google API) with the right exercise commands at the right time and with proper breaks. Other than that, communicating the Arduino over the serial with Python was a bit hectic. 

## Accomplishments that we're proud of
Overcoming the mentioned challenges like that of the hardware malfunctioning and software synching was a great accomplishment for us in itself. Another mentionable achievement was completing the entire project on time, along with getting the desired and optimized results from our project prototype. 

## What we learned
We learned about communicating the hardware i.e. the Arduino with Python. We also learned about the setting up of Google's Text-to-Speech API. 

## What's next for Gym Bot
In the future, we will try to improve the monitoring system which will observe the user during performing of the exercises and prompt the mistakes in postures being made, as well as monitor the improvement of physical health and suggest a change in the workout chart with proper reps accordingly. 
