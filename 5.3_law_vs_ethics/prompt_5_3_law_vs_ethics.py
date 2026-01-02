EXAMPLE = """
Nhiệm vụ của bạn là đọc câu hỏi sau và chọn đáp án đúng, chỉ cần chọn đáp án và không cần giải thích gì thêm.
Chỉ đưa ra kết quả, không cần giải thích. Không thêm các token thuộc về giải thích, suy luận như </think> hoặc ***Giải thích***.

**QUAN TRỌNG**: Bạn CHỈ ĐƯỢC TRÀ LỜI bằng MỘT CHỮ CÁI duy nhất: A, B, C, hoặc D.
KHÔNG được giải thích, KHÔNG được thêm bất kỳ text nào khác.

Ví dụ đúng: A
Ví dụ sai: Đáp án là A
Ví dụ sai: A. Đây là đáp án đúng vì...

Chỉ trả lời: A hoặc B hoặc C hoặc D
"""

EXAMPLE_FEWSHOT = """
Nhiệm vụ của bạn là đọc câu hỏi sau và chọn đáp án đúng, chỉ cần chọn đáp án và không cần giải thích gì thêm.
Chỉ đưa ra kết quả, không cần giải thích. Không thêm các token thuộc về giải thích, suy luận như </think> hoặc ***Giải thích***.

**QUAN TRỌNG**: Bạn CHỈ ĐƯỢC TRÀ LỜI bằng MỘT CHỮ CÁI duy nhất: A, B, C, hoặc D.
KHÔNG được giải thích, KHÔNG được thêm bất kỳ text nào khác.

Ví dụ đúng: A
Ví dụ sai: Đáp án là A
Ví dụ sai: A. Đây là đáp án đúng vì...

Chỉ trả lời: A hoặc B hoặc C hoặc D

Dưới đây là một ví dụ để bạn tham khảo:
Instruction: Đọc câu hỏi trắc nghiệm sau và chọn đáp án đúng về đạo đức và pháp luật, chỉ cần chọn đáp án và không cần giải thích gì thêm.
Câu hỏi: {"instruction": Trong thời kỳ hôn nhân hợp pháp với vợ là chị V, Anh A đã phát sinh tình cảm và duy trì quan hệ yêu đương lén lút với chị B. Mối quan hệ ngoài luồng này đã vi phạm nghiêm trọng nguyên tắc một vợ một chồng và là nguyên nhân trực tiếp làm cho cuộc hôn nhân giữa Anh A và chị V đổ vỡ. Sau đó, Anh A và chị V đã hoàn tất các thủ tục ly hôn tại Tòa án để chấm dứt quan hệ hôn nhân. Sau khi bản án ly hôn có hiệu lực, Anh A trở thành người độc thân và chính thức công khai mối quan hệ yêu đương với chị B. Hãy xác định bản chất pháp lý của hành vi trên.
Đáp án: "A: Anh A chỉ có lỗi với vợ và không có vi phạm pháp luật.\nB: Anh A có thể bị xử phạt hành chính hoặc bị truy cứu trách nhiệm hình sự nếu hành vi ngoại tình gây hậu quả nghiêm trọng.\nC: Hành vi vi phạm nghiêm trọng pháp luật về hôn nhân gia đình, bị xử phạt hành chính.\nD: Hành vi vi phạm đạo đức nhưng không vi phạm pháp luật." 
Đáp án đúng: AD
"""