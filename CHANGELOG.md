# Changelog

Tất cả các thay đổi quan trọng trong project sẽ được ghi lại trong file này.

## [2.0.0] - 2024-12-19

### 🆕 Tính năng mới
- **Universal Audio Support**: Bot giờ có thể phát âm thanh từ nhiều nguồn khác nhau:
  - YouTube (video và playlist)
  - SoundCloud (track và playlist)
  - Spotify (track và album)
  - Direct audio links (.mp3, .wav, .flac, .m4a, .ogg)
  - File upload từ Discord

- **Lệnh mới**:
  - `$playfile` - Phát âm thanh từ file được upload
  - Cải tiến `$play` để hỗ trợ nhiều nguồn âm thanh

### 🔧 Cải tiến
- **Enhanced Audio Detection**: Tự động nhận diện nguồn âm thanh và hiển thị thông tin chi tiết
- **Better Error Handling**: Thông báo lỗi rõ ràng hơn và hướng dẫn khắc phục
- **Improved UI**: Embed messages hiển thị thông tin nguồn âm thanh
- **Queue Management**: Cải thiện quản lý queue với thông tin đầy đủ

### 🐛 Sửa lỗi
- Sửa lỗi xử lý URL không hợp lệ
- Cải thiện xử lý lỗi khi phát âm thanh
- Sửa lỗi hiển thị thông tin âm thanh

### 📝 Thay đổi
- Đổi tên từ "Music Player" thành "Audio Player" để phản ánh tính năng mới
- Cập nhật tất cả thông báo từ "bài hát" thành "âm thanh"
- Cải thiện documentation và README

## [1.0.0] - 2024-12-18

### 🎉 Phiên bản đầu tiên
- **AI Chat**: Tích hợp Google Gemini AI
- **YouTube Music Player**: Phát nhạc từ YouTube
- **Voice Commands**: Điều khiển nhạc qua voice channel
- **Auto-moderation**: Tự động xóa tin nhắn không phù hợp
- **Queue System**: Quản lý danh sách phát
- **Basic Commands**: play, search, skip, pause, resume, stop, queue, volume, etc.

---

## Cách sử dụng phiên bản mới

### Chạy phiên bản Enhanced:
```bash
python main_enhanced.py
```

### Chạy phiên bản cũ:
```bash
python main.py
```

### Tính năng mới trong phiên bản Enhanced:

1. **Phát âm thanh từ bất kỳ link nào**:
   ```
   $play https://youtube.com/watch?v=...
   $play https://soundcloud.com/...
   $play https://open.spotify.com/track/...
   $play https://example.com/audio.mp3
   ```

2. **Phát âm thanh từ file upload**:
   ```
   [Upload file âm thanh]
   $playfile
   ```

3. **Thông tin chi tiết**: Bot sẽ hiển thị nguồn âm thanh và thông tin đầy đủ

## Migration Guide

Nếu bạn đang sử dụng phiên bản cũ (`main.py`), bạn có thể:

1. **Giữ nguyên**: Tiếp tục sử dụng `main.py` nếu chỉ cần phát YouTube
2. **Nâng cấp**: Chuyển sang `main_enhanced.py` để có thêm tính năng mới

Không có breaking changes, tất cả lệnh cũ vẫn hoạt động bình thường.
