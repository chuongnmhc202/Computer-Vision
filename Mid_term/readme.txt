Mục tiêu của bài toán là phân loại hình ảnh Cifar-10 thành 10 Predicted Label

Hiệu suất CNN cải thiện liên tục qua từng epoch với độ chính xác tăng dần. 
Hiệu suất của AE giảm loss qua từng epoch cho thấy mô hình cũng đang học tốt. Tuy nhiên, độ chính xác trên tập val thấp so với CNN khi so sánh.
=> CNN có khả năng tốt hơn do kiến trúc của nó được thiết kế để xử lý tác vụ này một cách hiệu quả, điều được thể hiện qua độ chính xác cao hơn trong quá trình validation.

Autoencoder
Training Loss: Giảm mạnh và liên tục qua từng epoch, cho thấy mô hình học tốt từ dữ liệu.
Validation Loss: Có xu hướng giảm nhưng không ổn định và bắt đầu tăng lên sau epoch thứ 10, điều này có thể là dấu hiệu của overfitting - mô hình tốt trên dữ liệu huấn luyện nhưng không khái quát hóa tốt trên dữ liệu kiểm định.

CNN
Training Loss: Giảm liên tục và mạnh mẽ, thể hiện rõ quá trình học.
Validation Loss: Cũng giảm tương tự như training loss, bắt đầu ổn định sau khoảng 10 epochs, cho thấy mô hình có khả năng khái quát hóa tốt.