//ใช้ nodejs นะครับ
//เอาคำสั่ง input
const readline = require("readline").createInterface({
    input: process.stdin,
    output: process.stdout,
});

//กำหนดคำสั่งเอง
String.prototype.replaceAt = function (index, replacement) {
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}

console.log("------LOVE NOTE-----")
readline.question("Please input your name : ", question => {
    var getText = question.toLowerCase(); //ปรับตัวอักษรเป็นพิมพ์เล็กหมด
    var text_count = getText.length; //นับจำนวนคำ
    function selectText(inputhere) {
        inputhere = getText.charAt(i - 1) //ดึงตัวอักษรตัวที่ n
        processing = inputhere.toUpperCase(); //ปรับตัวอักษรที่ดึงมาเป็นตัวพิมพ์ใหญ่
        final = getText.replaceAt(i - 1, processing) //นำตัวอักษรที่ปรับแล้วแทนที่ตัวอักษรเดิม
        return (
            console.log(final)
        )
    }
    for (i = 1; i <= text_count; i++) {
        selectText(getText) //เรียกใช้ฟังก์ชัน selectText
    } //ลูปตามจำนวนตัวอักษร
    readline.close();
})