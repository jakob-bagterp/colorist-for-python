---
tags:
    - Documentation
    - Tutorial
    - ANSI Escape Codes
    - Extended 256 Colors
---

# Extended 256 Colors in ANSI Escape Codes
The [extended palette of 256 colors](https://commons.wikimedia.org/wiki/File:Xterm_256color_chart.svg) is a 6x6x6 color cube, with 216 colors, plus 24 shades of gray. The color cube is made up of 6 levels of red, green, and blue, respectively. The color cube is then combined with the 24 shades of gray to make up the 256 colors.

It works both with foreground text and background colors. Simply replace the three underscores `___` with any number from `000` to `255`:

| Code            | Placement  |
| :-------------: | :--------: |
| `\x1b[38;5;___m` | Text       |
| `\x1b[48;5;___m` | Background |

For example, `\x1b[38;5;243m` is a light gray foreground text color, and `\x1b[48;5;243m` is a light gray background color.

## Cheat Sheets
### Standard Colors

<table>
    <tbody>
        <tr>
            <td style="background-color: #000000">000</td>
            <td style="background-color: #800000">001</td>
            <td style="background-color: #008000">002</td>
            <td style="background-color: #808000">003</td>
            <td style="background-color: #000080">004</td>
            <td style="background-color: #800080">005</td>
            <td style="background-color: #008080">006</td>
            <td style="background-color: #c0c0c0">007</td>
        </tr>
        <tr>
            <td style="background-color: #808080">008</td>
            <td style="background-color: #ff0000">009</td>
            <td style="background-color: #00ff00">010</td>
            <td style="background-color: #ffff00">011</td>
            <td style="background-color: #0000ff">012</td>
            <td style="background-color: #ff00ff">013</td>
            <td style="background-color: #00ffff">014</td>
            <td style="background-color: #ffffff">015</td>
        </tr>
    </tbody>
</table>

### Grey Scale

<table>
    <tbody>
        <tr>
            <td style="background-color: #080808">232</td>
            <td style="background-color: #121212">233</td>
            <td style="background-color: #1c1c1c">234</td>
            <td style="background-color: #262626">235</td>
            <td style="background-color: #303030">236</td>
            <td style="background-color: #3a3a3a">237</td>
            <td style="background-color: #444444">238</td>
            <td style="background-color: #4e4e4e">239</td>
            <td style="background-color: #585858">240</td>
            <td style="background-color: #626262">241</td>
            <td style="background-color: #6c6c6c">242</td>
            <td style="background-color: #767676">243</td>
        </tr>
        <tr>
            <td style="background-color: #808080">244</td>
            <td style="background-color: #8a8a8a">245</td>
            <td style="background-color: #949494">246</td>
            <td style="background-color: #9e9e9e">247</td>
            <td style="background-color: #a8a8a8">248</td>
            <td style="background-color: #b2b2b2">249</td>
            <td style="background-color: #bcbcbc">250</td>
            <td style="background-color: #c6c6c6">251</td>
            <td style="background-color: #d0d0d0">252</td>
            <td style="background-color: #dadada">253</td>
            <td style="background-color: #e4e4e4">254</td>
            <td style="background-color: #eeeeee">255</td>
        </tr>
    </tbody>
</table>

### Extended Colors

<table>
    <tbody>
        <tr>
            <td style="background-color: #000000">016</td>
            <td style="background-color: #00005f">017</td>
            <td style="background-color: #000087">018</td>
            <td style="background-color: #0000af">019</td>
            <td style="background-color: #0000d7">020</td>
            <td style="background-color: #0000ff">021</td>
        </tr>
        <tr>
            <td style="background-color: #005f00">022</td>
            <td style="background-color: #005f5f">023</td>
            <td style="background-color: #005f87">024</td>
            <td style="background-color: #005faf">025</td>
            <td style="background-color: #005fd7">026</td>
            <td style="background-color: #005fff">027</td>
        </tr>
        <tr>
            <td style="background-color: #008700">028</td>
            <td style="background-color: #00875f">029</td>
            <td style="background-color: #008787">030</td>
            <td style="background-color: #0087af">031</td>
            <td style="background-color: #0087d7">032</td>
            <td style="background-color: #0087ff">033</td>
        </tr>
        <tr>
            <td style="background-color: #00af00">034</td>
            <td style="background-color: #00af5f">035</td>
            <td style="background-color: #00af87">036</td>
            <td style="background-color: #00afaf">037</td>
            <td style="background-color: #00afd7">038</td>
            <td style="background-color: #00afff">039</td>
        </tr>
        <tr>
            <td style="background-color: #00d700">040</td>
            <td style="background-color: #00d75f">041</td>
            <td style="background-color: #00d787">042</td>
            <td style="background-color: #00d7af">043</td>
            <td style="background-color: #00d7d7">044</td>
            <td style="background-color: #00d7ff">045</td>
        </tr>
        <tr>
            <td style="background-color: #00ff00">046</td>
            <td style="background-color: #00ff5f">047</td>
            <td style="background-color: #00ff87">048</td>
            <td style="background-color: #00ffaf">049</td>
            <td style="background-color: #00ffd7">050</td>
            <td style="background-color: #00ffff">051</td>
        </tr>
        <tr>
            <td style="background-color: #5f0000">052</td>
            <td style="background-color: #5f005f">053</td>
            <td style="background-color: #5f0087">054</td>
            <td style="background-color: #5f00af">055</td>
            <td style="background-color: #5f00d7">056</td>
            <td style="background-color: #5f00ff">057</td>
        </tr>
        <tr>
            <td style="background-color: #5f5f00">058</td>
            <td style="background-color: #5f5f5f">059</td>
            <td style="background-color: #5f5f87">060</td>
            <td style="background-color: #5f5faf">061</td>
            <td style="background-color: #5f5fd7">062</td>
            <td style="background-color: #5f5fff">063</td>
        </tr>
        <tr>
            <td style="background-color: #5f8700">064</td>
            <td style="background-color: #5f875f">065</td>
            <td style="background-color: #5f8787">066</td>
            <td style="background-color: #5f87af">067</td>
            <td style="background-color: #5f87d7">068</td>
            <td style="background-color: #5f87ff">069</td>
        </tr>
        <tr>
            <td style="background-color: #5faf00">070</td>
            <td style="background-color: #5faf5f">071</td>
            <td style="background-color: #5faf87">072</td>
            <td style="background-color: #5fafaf">073</td>
            <td style="background-color: #5fafd7">074</td>
            <td style="background-color: #5fafff">075</td>
        </tr>
        <tr>
            <td style="background-color: #5fd700">076</td>
            <td style="background-color: #5fd75f">077</td>
            <td style="background-color: #5fd787">078</td>
            <td style="background-color: #5fd7af">079</td>
            <td style="background-color: #5fd7d7">080</td>
            <td style="background-color: #5fd7ff">081</td>
        </tr>
        <tr>
            <td style="background-color: #5fff00">082</td>
            <td style="background-color: #5fff5f">083</td>
            <td style="background-color: #5fff87">084</td>
            <td style="background-color: #5fffaf">085</td>
            <td style="background-color: #5fffd7">086</td>
            <td style="background-color: #5fffff">087</td>
        </tr>
        <tr>
            <td style="background-color: #870000">088</td>
            <td style="background-color: #87005f">089</td>
            <td style="background-color: #870087">090</td>
            <td style="background-color: #8700af">091</td>
            <td style="background-color: #8700d7">092</td>
            <td style="background-color: #8700ff">093</td>
        </tr>
        <tr>
            <td style="background-color: #875f00">094</td>
            <td style="background-color: #875f5f">095</td>
            <td style="background-color: #875f87">096</td>
            <td style="background-color: #875faf">097</td>
            <td style="background-color: #875fd7">098</td>
            <td style="background-color: #875fff">099</td>
        </tr>
        <tr>
            <td style="background-color: #878700">100</td>
            <td style="background-color: #87875f">101</td>
            <td style="background-color: #878787">102</td>
            <td style="background-color: #8787af">103</td>
            <td style="background-color: #8787d7">104</td>
            <td style="background-color: #8787ff">105</td>
        </tr>
        <tr>
            <td style="background-color: #87af00">106</td>
            <td style="background-color: #87af5f">107</td>
            <td style="background-color: #87af87">108</td>
            <td style="background-color: #87afaf">109</td>
            <td style="background-color: #87afd7">110</td>
            <td style="background-color: #87afff">111</td>
        </tr>
        <tr>
            <td style="background-color: #87d700">112</td>
            <td style="background-color: #87d75f">113</td>
            <td style="background-color: #87d787">114</td>
            <td style="background-color: #87d7af">115</td>
            <td style="background-color: #87d7d7">116</td>
            <td style="background-color: #87d7ff">117</td>
        </tr>
        <tr>
            <td style="background-color: #87ff00">118</td>
            <td style="background-color: #87ff5f">119</td>
            <td style="background-color: #87ff87">120</td>
            <td style="background-color: #87ffaf">121</td>
            <td style="background-color: #87ffd7">122</td>
            <td style="background-color: #87ffff">123</td>
        </tr>
        <tr>
            <td style="background-color: #af0000">124</td>
            <td style="background-color: #af005f">125</td>
            <td style="background-color: #af0087">126</td>
            <td style="background-color: #af00af">127</td>
            <td style="background-color: #af00d7">128</td>
            <td style="background-color: #af00ff">129</td>
        </tr>
        <tr>
            <td style="background-color: #af5f00">130</td>
            <td style="background-color: #af5f5f">131</td>
            <td style="background-color: #af5f87">132</td>
            <td style="background-color: #af5faf">133</td>
            <td style="background-color: #af5fd7">134</td>
            <td style="background-color: #af5fff">135</td>
        </tr>
        <tr>
            <td style="background-color: #af8700">136</td>
            <td style="background-color: #af875f">137</td>
            <td style="background-color: #af8787">138</td>
            <td style="background-color: #af87af">139</td>
            <td style="background-color: #af87d7">140</td>
            <td style="background-color: #af87ff">141</td>
        </tr>
        <tr>
            <td style="background-color: #afaf00">142</td>
            <td style="background-color: #afaf5f">143</td>
            <td style="background-color: #afaf87">144</td>
            <td style="background-color: #afafaf">145</td>
            <td style="background-color: #afafd7">146</td>
            <td style="background-color: #afafff">147</td>
        </tr>
        <tr>
            <td style="background-color: #afd700">148</td>
            <td style="background-color: #afd75f">149</td>
            <td style="background-color: #afd787">150</td>
            <td style="background-color: #afd7af">151</td>
            <td style="background-color: #afd7d7">152</td>
            <td style="background-color: #afd7ff">153</td>
        </tr>
        <tr>
            <td style="background-color: #afff00">154</td>
            <td style="background-color: #afff5f">155</td>
            <td style="background-color: #afff87">156</td>
            <td style="background-color: #afffaf">157</td>
            <td style="background-color: #afffd7">158</td>
            <td style="background-color: #afffff">159</td>
        </tr>
        <tr>
            <td style="background-color: #d70000">160</td>
            <td style="background-color: #d7005f">161</td>
            <td style="background-color: #d70087">162</td>
            <td style="background-color: #d700af">163</td>
            <td style="background-color: #d700d7">164</td>
            <td style="background-color: #d700ff">165</td>
        </tr>
        <tr>
            <td style="background-color: #d75f00">166</td>
            <td style="background-color: #d75f5f">167</td>
            <td style="background-color: #d75f87">168</td>
            <td style="background-color: #d75faf">169</td>
            <td style="background-color: #d75fd7">170</td>
            <td style="background-color: #d75fff">171</td>
        </tr>
        <tr>
            <td style="background-color: #d78700">172</td>
            <td style="background-color: #d7875f">173</td>
            <td style="background-color: #d78787">174</td>
            <td style="background-color: #d787af">175</td>
            <td style="background-color: #d787d7">176</td>
            <td style="background-color: #d787ff">177</td>
        </tr>
        <tr>
            <td style="background-color: #d7af00">178</td>
            <td style="background-color: #d7af5f">179</td>
            <td style="background-color: #d7af87">180</td>
            <td style="background-color: #d7afaf">181</td>
            <td style="background-color: #d7afd7">182</td>
            <td style="background-color: #d7afff">183</td>
        </tr>
        <tr>
            <td style="background-color: #d7d700">184</td>
            <td style="background-color: #d7d75f">185</td>
            <td style="background-color: #d7d787">186</td>
            <td style="background-color: #d7d7af">187</td>
            <td style="background-color: #d7d7d7">188</td>
            <td style="background-color: #d7d7ff">189</td>
        </tr>
        <tr>
            <td style="background-color: #d7ff00">190</td>
            <td style="background-color: #d7ff5f">191</td>
            <td style="background-color: #d7ff87">192</td>
            <td style="background-color: #d7ffaf">193</td>
            <td style="background-color: #d7ffd7">194</td>
            <td style="background-color: #d7ffff">195</td>
        </tr>
        <tr>
            <td style="background-color: #ff0000">196</td>
            <td style="background-color: #ff005f">197</td>
            <td style="background-color: #ff0087">198</td>
            <td style="background-color: #ff00af">199</td>
            <td style="background-color: #ff00d7">200</td>
            <td style="background-color: #ff00ff">201</td>
        </tr>
        <tr>
            <td style="background-color: #ff5f00">202</td>
            <td style="background-color: #ff5f5f">203</td>
            <td style="background-color: #ff5f87">204</td>
            <td style="background-color: #ff5faf">205</td>
            <td style="background-color: #ff5fd7">206</td>
            <td style="background-color: #ff5fff">207</td>
        </tr>
        <tr>
            <td style="background-color: #ff8700">208</td>
            <td style="background-color: #ff875f">209</td>
            <td style="background-color: #ff8787">210</td>
            <td style="background-color: #ff87af">211</td>
            <td style="background-color: #ff87d7">212</td>
            <td style="background-color: #ff87ff">213</td>
        </tr>
        <tr>
            <td style="background-color: #ffaf00">214</td>
            <td style="background-color: #ffaf5f">215</td>
            <td style="background-color: #ffaf87">216</td>
            <td style="background-color: #ffafaf">217</td>
            <td style="background-color: #ffafd7">218</td>
            <td style="background-color: #ffafff">219</td>
        </tr>
        <tr>
            <td style="background-color: #ffd700">220</td>
            <td style="background-color: #ffd75f">221</td>
            <td style="background-color: #ffd787">222</td>
            <td style="background-color: #ffd7af">223</td>
            <td style="background-color: #ffd7d7">224</td>
            <td style="background-color: #ffd7ff">225</td>
        </tr>
        <tr>
            <td style="background-color: #ffff00">226</td>
            <td style="background-color: #ffff5f">227</td>
            <td style="background-color: #ffff87">228</td>
            <td style="background-color: #ffffaf">229</td>
            <td style="background-color: #ffffd7">230</td>
            <td style="background-color: #ffffff">231</td>
        </tr>
    </tbody>
</table>
