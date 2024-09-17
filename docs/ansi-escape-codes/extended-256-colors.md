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
### Standard Palette

<table>
    <tbody>
        <tr>
            <td class="extcol-000">000</td>
            <td class="extcol-001">001</td>
            <td class="extcol-002">002</td>
            <td class="extcol-003">003</td>
            <td class="extcol-004">004</td>
            <td class="extcol-005">005</td>
            <td class="extcol-006">006</td>
            <td class="extcol-007">007</td>
        </tr>
        <tr>
            <td class="extcol-008">008</td>
            <td class="extcol-009">009</td>
            <td class="extcol-010">010</td>
            <td class="extcol-011">011</td>
            <td class="extcol-012">012</td>
            <td class="extcol-013">013</td>
            <td class="extcol-014">014</td>
            <td class="extcol-015">015</td>
        </tr>
    </tbody>
</table>

### Gray Scale

<table>
    <tbody>
        <tr>
            <td class="extcol-232">232</td>
            <td class="extcol-233">233</td>
            <td class="extcol-234">234</td>
            <td class="extcol-235">235</td>
            <td class="extcol-236">236</td>
            <td class="extcol-237">237</td>
            <td class="extcol-238">238</td>
            <td class="extcol-239">239</td>
        </tr>
        <tr>
            <td class="extcol-240">240</td>
            <td class="extcol-241">241</td>
            <td class="extcol-242">242</td>
            <td class="extcol-243">243</td>
            <td class="extcol-244">244</td>
            <td class="extcol-245">245</td>
            <td class="extcol-246">246</td>
            <td class="extcol-247">247</td>
        </tr>
        <tr>
            <td class="extcol-248">248</td>
            <td class="extcol-249">249</td>
            <td class="extcol-250">250</td>
            <td class="extcol-251">251</td>
            <td class="extcol-252">252</td>
            <td class="extcol-253">253</td>
            <td class="extcol-254">254</td>
            <td class="extcol-255">255</td>
        </tr>
        </tbody>
</table>

### Extended Palette

<table>
    <tbody>
        <tr>
            <td class="extcol-016">016</td>
            <td class="extcol-017">017</td>
            <td class="extcol-018">018</td>
            <td class="extcol-019">019</td>
            <td class="extcol-020">020</td>
            <td class="extcol-021">021</td>
        </tr>
        <tr>
            <td class="extcol-022">022</td>
            <td class="extcol-023">023</td>
            <td class="extcol-024">024</td>
            <td class="extcol-025">025</td>
            <td class="extcol-026">026</td>
            <td class="extcol-027">027</td>
        </tr>
        <tr>
            <td class="extcol-028">028</td>
            <td class="extcol-029">029</td>
            <td class="extcol-030">030</td>
            <td class="extcol-031">031</td>
            <td class="extcol-032">032</td>
            <td class="extcol-033">033</td>
        </tr>
        <tr>
            <td class="extcol-034">034</td>
            <td class="extcol-035">035</td>
            <td class="extcol-036">036</td>
            <td class="extcol-037">037</td>
            <td class="extcol-038">038</td>
            <td class="extcol-039">039</td>
        </tr>
        <tr>
            <td class="extcol-040">040</td>
            <td class="extcol-041">041</td>
            <td class="extcol-042">042</td>
            <td class="extcol-043">043</td>
            <td class="extcol-044">044</td>
            <td class="extcol-045">045</td>
        </tr>
        <tr>
            <td class="extcol-046">046</td>
            <td class="extcol-047">047</td>
            <td class="extcol-048">048</td>
            <td class="extcol-049">049</td>
            <td class="extcol-050">050</td>
            <td class="extcol-051">051</td>
        </tr>
        <tr>
            <td class="extcol-052">052</td>
            <td class="extcol-053">053</td>
            <td class="extcol-054">054</td>
            <td class="extcol-055">055</td>
            <td class="extcol-056">056</td>
            <td class="extcol-057">057</td>
        </tr>
        <tr>
            <td class="extcol-058">058</td>
            <td class="extcol-059">059</td>
            <td class="extcol-060">060</td>
            <td class="extcol-061">061</td>
            <td class="extcol-062">062</td>
            <td class="extcol-063">063</td>
        </tr>
        <tr>
            <td class="extcol-064">064</td>
            <td class="extcol-065">065</td>
            <td class="extcol-066">066</td>
            <td class="extcol-067">067</td>
            <td class="extcol-068">068</td>
            <td class="extcol-069">069</td>
        </tr>
        <tr>
            <td class="extcol-070">070</td>
            <td class="extcol-071">071</td>
            <td class="extcol-072">072</td>
            <td class="extcol-073">073</td>
            <td class="extcol-074">074</td>
            <td class="extcol-075">075</td>
        </tr>
        <tr>
            <td class="extcol-076">076</td>
            <td class="extcol-077">077</td>
            <td class="extcol-078">078</td>
            <td class="extcol-079">079</td>
            <td class="extcol-080">080</td>
            <td class="extcol-081">081</td>
        </tr>
        <tr>
            <td class="extcol-082">082</td>
            <td class="extcol-083">083</td>
            <td class="extcol-084">084</td>
            <td class="extcol-085">085</td>
            <td class="extcol-086">086</td>
            <td class="extcol-087">087</td>
        </tr>
        <tr>
            <td class="extcol-088">088</td>
            <td class="extcol-089">089</td>
            <td class="extcol-090">090</td>
            <td class="extcol-091">091</td>
            <td class="extcol-092">092</td>
            <td class="extcol-093">093</td>
        </tr>
        <tr>
            <td class="extcol-094">094</td>
            <td class="extcol-095">095</td>
            <td class="extcol-096">096</td>
            <td class="extcol-097">097</td>
            <td class="extcol-098">098</td>
            <td class="extcol-099">099</td>
        </tr>
        <tr>
            <td class="extcol-100">100</td>
            <td class="extcol-101">101</td>
            <td class="extcol-102">102</td>
            <td class="extcol-103">103</td>
            <td class="extcol-104">104</td>
            <td class="extcol-105">105</td>
        </tr>
        <tr>
            <td class="extcol-106">106</td>
            <td class="extcol-107">107</td>
            <td class="extcol-108">108</td>
            <td class="extcol-109">109</td>
            <td class="extcol-110">110</td>
            <td class="extcol-111">111</td>
        </tr>
        <tr>
            <td class="extcol-112">112</td>
            <td class="extcol-113">113</td>
            <td class="extcol-114">114</td>
            <td class="extcol-115">115</td>
            <td class="extcol-116">116</td>
            <td class="extcol-117">117</td>
        </tr>
        <tr>
            <td class="extcol-118">118</td>
            <td class="extcol-119">119</td>
            <td class="extcol-120">120</td>
            <td class="extcol-121">121</td>
            <td class="extcol-122">122</td>
            <td class="extcol-123">123</td>
        </tr>
        <tr>
            <td class="extcol-124">124</td>
            <td class="extcol-125">125</td>
            <td class="extcol-126">126</td>
            <td class="extcol-127">127</td>
            <td class="extcol-128">128</td>
            <td class="extcol-129">129</td>
        </tr>
        <tr>
            <td class="extcol-130">130</td>
            <td class="extcol-131">131</td>
            <td class="extcol-132">132</td>
            <td class="extcol-133">133</td>
            <td class="extcol-134">134</td>
            <td class="extcol-135">135</td>
        </tr>
        <tr>
            <td class="extcol-136">136</td>
            <td class="extcol-137">137</td>
            <td class="extcol-138">138</td>
            <td class="extcol-139">139</td>
            <td class="extcol-140">140</td>
            <td class="extcol-141">141</td>
        </tr>
        <tr>
            <td class="extcol-142">142</td>
            <td class="extcol-143">143</td>
            <td class="extcol-144">144</td>
            <td class="extcol-145">145</td>
            <td class="extcol-146">146</td>
            <td class="extcol-147">147</td>
        </tr>
        <tr>
            <td class="extcol-148">148</td>
            <td class="extcol-149">149</td>
            <td class="extcol-150">150</td>
            <td class="extcol-151">151</td>
            <td class="extcol-152">152</td>
            <td class="extcol-153">153</td>
        </tr>
        <tr>
            <td class="extcol-154">154</td>
            <td class="extcol-155">155</td>
            <td class="extcol-156">156</td>
            <td class="extcol-157">157</td>
            <td class="extcol-158">158</td>
            <td class="extcol-159">159</td>
        </tr>
        <tr>
            <td class="extcol-160">160</td>
            <td class="extcol-161">161</td>
            <td class="extcol-162">162</td>
            <td class="extcol-163">163</td>
            <td class="extcol-164">164</td>
            <td class="extcol-165">165</td>
        </tr>
        <tr>
            <td class="extcol-166">166</td>
            <td class="extcol-167">167</td>
            <td class="extcol-168">168</td>
            <td class="extcol-169">169</td>
            <td class="extcol-170">170</td>
            <td class="extcol-171">171</td>
        </tr>
        <tr>
            <td class="extcol-172">172</td>
            <td class="extcol-173">173</td>
            <td class="extcol-174">174</td>
            <td class="extcol-175">175</td>
            <td class="extcol-176">176</td>
            <td class="extcol-177">177</td>
        </tr>
        <tr>
            <td class="extcol-178">178</td>
            <td class="extcol-179">179</td>
            <td class="extcol-180">180</td>
            <td class="extcol-181">181</td>
            <td class="extcol-182">182</td>
            <td class="extcol-183">183</td>
        </tr>
        <tr>
            <td class="extcol-184">184</td>
            <td class="extcol-185">185</td>
            <td class="extcol-186">186</td>
            <td class="extcol-187">187</td>
            <td class="extcol-188">188</td>
            <td class="extcol-189">189</td>
        </tr>
        <tr>
            <td class="extcol-190">190</td>
            <td class="extcol-191">191</td>
            <td class="extcol-192">192</td>
            <td class="extcol-193">193</td>
            <td class="extcol-194">194</td>
            <td class="extcol-195">195</td>
        </tr>
        <tr>
            <td class="extcol-196">196</td>
            <td class="extcol-197">197</td>
            <td class="extcol-198">198</td>
            <td class="extcol-199">199</td>
            <td class="extcol-200">200</td>
            <td class="extcol-201">201</td>
        </tr>
        <tr>
            <td class="extcol-202">202</td>
            <td class="extcol-203">203</td>
            <td class="extcol-204">204</td>
            <td class="extcol-205">205</td>
            <td class="extcol-206">206</td>
            <td class="extcol-207">207</td>
        </tr>
        <tr>
            <td class="extcol-208">208</td>
            <td class="extcol-209">209</td>
            <td class="extcol-210">210</td>
            <td class="extcol-211">211</td>
            <td class="extcol-212">212</td>
            <td class="extcol-213">213</td>
        </tr>
        <tr>
            <td class="extcol-214">214</td>
            <td class="extcol-215">215</td>
            <td class="extcol-216">216</td>
            <td class="extcol-217">217</td>
            <td class="extcol-218">218</td>
            <td class="extcol-219">219</td>
        </tr>
        <tr>
            <td class="extcol-220">220</td>
            <td class="extcol-221">221</td>
            <td class="extcol-222">222</td>
            <td class="extcol-223">223</td>
            <td class="extcol-224">224</td>
            <td class="extcol-225">225</td>
        </tr>
        <tr>
            <td class="extcol-226">226</td>
            <td class="extcol-227">227</td>
            <td class="extcol-228">228</td>
            <td class="extcol-229">229</td>
            <td class="extcol-230">230</td>
            <td class="extcol-231">231</td>
        </tr>
    </tbody>
</table>
