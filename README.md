# CalHacksApp
Hack at Cal Hacks

{% if sentiment.score < 20 and sentiment.score >= -20 %}
            <p>The current opinion on this company appears pretty neutral. We reccomend you keep the stocks.</p>
          {% endif %}

          {% if sentiment.score < 40 and sentiment.score >= 20  %}
            <p>The company seems to be on a positive trend. We reccomend you to consider investing more into this company.</p>
          {% endif %}

          {% if sentiment.score < 75  and sentiment.score >= 40%}
            <p>The company seems to have a great outlook based on current public opinion. You may want to start considering selling your stocks for this company.</p>
          {% endif %}

          {% if sentiment.score > 75 %}
            <p>This company appears to be at a all time high and the bubble may soon burst. This is a great time to sell your stocks as demand for this company is high based on public opinion.</p>
          {% endif %}

          {% if sentiment.score < -20 and sentiment.score >= -40 %}
            <p>This company appears to be on the down side. Consider either selling or holding out on this minor low.</p>
          {% endif %}

          {% if sentiment.score < -40 and sentiment.score >= -75 %}
            <p>Things are really not looking too great. We reccomend you to sell your stocks as the public really is starting to lose trust in this company.</p>
          {% endif %}

          {% if sentiment.score < -75 %}
            <p>Public opinion for this company is nearing the bottom. It definitely is time to sell all your stocks before the stock prices drop even lower!</p>
          {% endif %}
