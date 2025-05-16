import Button from "./button";
import { useRef, useState } from "react";

// generic OTP component which take number of input sub box as arg
export default function OTP({ number }) {
    // creating a ref which contains an array which will will be binded to reference of each DOM subOtpBox 
    const ref = useRef(Array(number).fill(0));
    // Array storing actual value of each subOtpBox
    const [inputBoxVal, setInputBoxVal] = useState(Array(number).fill(""));
    // used to set the submit btn 
    const [disabled, setDisabled] = useState(true);

    return <div className="flex flex-col items-center">
        <div className="flex justify-center gap-2">

            {Array(number).fill(1).map((_, idx) =>
                <SubOtpBox
                    key={idx}
                    idx={idx}
                    inputBoxVal={inputBoxVal}
                    setInputBoxVal={setInputBoxVal}
                    reference={(e) => ref.current[idx] = e}
                    refer={ref}
                    setDisabled={setDisabled}
                />
            )}
        </div>
        <br />

        <Button disabled={disabled}>Sign up</Button>
    </div>;
}

function SubOtpBox({ reference, refer, idx, inputBoxVal, setInputBoxVal, setDisabled }) {
    const arrLen = inputBoxVal.length;
    return <div>
        <input
            maxLength={1}
            value={inputBoxVal[idx]}
            ref={reference}
            onKeyUp={(e) => {
                if (e.key == "Backspace") {
                    setDisabled(true);
                    // last digit case when all digits are filled; on backspace, cursor don't move, only current digit is emptied. 
                    if (idx + 1 == inputBoxVal.length && inputBoxVal[arrLen - 1] != "") {
                        setInputBoxVal((prev) => {
                            const copy = [...prev];
                            copy[idx] = "";
                            return copy;
                        });
                    }
                    // backspace usual case i.e. move cursor from current box to prev and empty prev digit box
                    else {
                        setInputBoxVal((prev) => {
                            const copy = [...prev];
                            copy[idx] = "";
                            copy[idx - 1] = "";
                            return copy;
                        });
                        if (idx == 0) return;
                        refer.current[idx - 1].focus(); // go to previous sub otp box to get next digit
                    }
                }
            }}

            onChange={(e) => {
                const inputDigit = e.target.value;
                // cheking if input is digit 0-9 value by comparing ascii value
                if (48 <= inputDigit.charCodeAt(0) && inputDigit.charCodeAt(0) <= 57) {
                    setInputBoxVal((prev) => {
                        const copy = [...prev];
                        copy[idx] = inputDigit;
                        return copy;
                    });
                    // enable the continue btn when all digits are provided
                    if (idx + 1 >= arrLen) {
                        setDisabled(false);
                        return;
                    };
                    refer.current[idx + 1].focus(); // go to next sub otp box to get next digit
                }
            }}
            type="text" className="px-4 w-[42px] h-[50px] outline-none font-bold rounded-2xl text-black bg-white" />
    </div>;
}