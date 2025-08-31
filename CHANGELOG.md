# Changelog

## [2.0.0] - 2024-12-19

### ✨ Tính năng mới
- **AI Chat Integration**: Tích hợp Google Gemini AI để trả lời câu hỏi
- **Music Player**: Hệ thống phát nhạc từ YouTube với queue system
- **Voice Commands**: Điều khiển nhạc qua voice channel
- **Auto-moderation**: Tự động xóa tin nhắn vi phạm

### 🔧 Cải tiến
- Cập nhật FFMPEG options để tối ưu audio streaming
- Thêm hệ thống queue management
- Cải thiện error handling và user feedback
- Tối ưu hóa performance cho audio streaming

### 🐛 Sửa lỗi
- Sửa lỗi connection timeout
- Cải thiện error messages
- Sửa lỗi queue management

### 📚 Tài liệu
- Cập nhật README.md với hướng dẫn chi tiết
- Thêm bảng lệnh đầy đủ
- Cập nhật phần troubleshooting
- Thêm ví dụ sử dụng

### 🎵 Lệnh mới
- `$start <câu hỏi>` - Hỏi AI
- `$play <URL>` - Phát nhạc từ YouTube
- `$search <từ khóa>` - Tìm kiếm và phát nhạc
- `$audio` - Bot tham gia kênh voice
- `$skip` - Bỏ qua bài hát hiện tại
- `$pause` - Tạm dừng bài hát
- `$resume` - Tiếp tục phát bài hát
- `$stop` - Dừng phát nhạc và xóa queue
- `$queue` - Hiển thị danh sách phát
- `$now` - Hiển thị bài hát đang phát
- `$remove <số>` - Xóa bài hát khỏi queue
- `$shuffle` - Xáo trộn queue
- `$volume [0-100]` - Điều chỉnh âm lượng
- `$leave` - Bot rời khỏi kênh voice

### ⚠️ Lưu ý
- Bot chỉ hỗ trợ audio streaming (không có video)
- Cần FFmpeg để phát nhạc từ YouTube
- Audio streaming tối ưu cho voice channels

## [1.0.0] - 2024-12-18

### 🎉 Phiên bản đầu tiên
- Bot Discord cơ bản với khả năng phát nhạc
- Hỗ trợ YouTube URLs
- Voice channel integration
- Basic music controls
