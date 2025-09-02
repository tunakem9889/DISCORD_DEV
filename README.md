# Discord Bot với AI và Audio Player

Một Discord bot đa chức năng với khả năng AI chat và phát âm thanh từ nhiều nguồn khác nhau.

## ✨ Tính năng chính

- **AI Chat**: Tích hợp Google Gemini AI để trả lời câu hỏi
- **Universal Audio Player**: Phát âm thanh từ YouTube, SoundCloud, Spotify, direct audio links và file upload
- **Voice Commands**: Điều khiển âm thanh qua voice channel
- **Auto-moderation**: Tự động xóa tin nhắn không phù hợp
- **File Upload Support**: Hỗ trợ phát âm thanh từ file được upload (.mp3, .wav, .flac, .m4a, .ogg)

## 🚀 Cài đặt

### 1. Clone repository
```bash
git clone <repository-url>
cd discord_dev
```

### 2. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 3. Cài đặt FFmpeg
Xem hướng dẫn chi tiết trong [FFMPEG_SETUP.md](FFMPEG_SETUP.md)

### 4. Tạo file .env
```bash
cp env_example.txt .env
```
Chỉnh sửa file `.env` với token Discord và API key Google AI:
```
DISCORD_TOKEN=your_discord_bot_token
GENAI_API_KEY=your_google_ai_api_key
```

### 5. Chạy bot
```bash
python main_enhanced.py
```

## 📋 Danh sách lệnh

### 📝 Lệnh cơ bản
| Lệnh | Mô tả | Ví dụ |
|------|-------|-------|
| `$hello` | Chào hỏi | `$hello` |
| `$helps` | Hiển thị danh sách lệnh | `$helps` |

### 🤖 Lệnh AI
| Lệnh | Mô tả | Ví dụ |
|------|-------|-------|
| `$start <câu hỏi>` | Hỏi AI | `$start Bạn có thể làm gì?` |

### 🎵 Lệnh Audio/Voice
| Lệnh | Mô tả | Ví dụ |
|------|-------|-------|
| `$play <URL>` | Phát âm thanh từ bất kỳ link nào | `$play https://youtube.com/watch?v=...` |
| `$playfile` | Phát âm thanh từ file upload | Upload file + `$playfile` |
| `$search <từ khóa>` | Tìm kiếm và phát âm thanh | `$search despacito` |
| `$audio` | Bot tham gia kênh thoại | `$audio` |
| `$skip` | Bỏ qua âm thanh hiện tại | `$skip` |
| `$pause` | Tạm dừng âm thanh | `$pause` |
| `$resume` | Tiếp tục phát âm thanh | `$resume` |
| `$stop` | Dừng phát và xóa queue | `$stop` |
| `$queue` | Hiển thị danh sách phát | `$queue` |
| `$now` | Hiển thị âm thanh đang phát | `$now` |
| `$remove <số>` | Xóa âm thanh khỏi queue | `$remove 2` |
| `$shuffle` | Xáo trộn queue | `$shuffle` |
| `$volume [0-100]` | Điều chỉnh âm lượng | `$volume 80` |
| `$leave` | Bot rời khỏi kênh voice | `$leave` |

## 🎯 Cách sử dụng

### 1. Khởi động bot
```
python main_enhanced.py
```

### 2. Tham gia voice channel
```
$audio
```

### 3. Phát âm thanh từ URL
```
$play https://youtube.com/watch?v=...
$play https://soundcloud.com/...
$play https://open.spotify.com/track/...
$play https://example.com/audio.mp3
```

### 4. Phát âm thanh từ file upload
```
[Upload file âm thanh (.mp3, .wav, .flac, .m4a, .ogg)]
$playfile
```

### 5. Tìm kiếm âm thanh
```
$search despacito
```

### 6. Điều khiển phát âm thanh
```
$skip      # Bỏ qua âm thanh
$pause     # Tạm dừng
$resume    # Tiếp tục
$stop      # Dừng hoàn toàn
```

### 7. Quản lý queue
```
$queue     # Xem danh sách
$remove 2  # Xóa âm thanh thứ 2
$shuffle   # Xáo trộn
```

### 8. Hỏi AI
```
$start Bạn có thể làm gì?
```

## 🌐 Hỗ trợ nguồn âm thanh

Bot hỗ trợ phát âm thanh từ các nguồn sau:

- **YouTube**: Video và playlist
- **SoundCloud**: Track và playlist
- **Spotify**: Track và album
- **Direct Audio Links**: File âm thanh trực tiếp (.mp3, .wav, .flac, .m4a, .ogg)
- **File Upload**: File âm thanh được upload lên Discord

## 🔧 Troubleshooting

### Bot không tham gia voice channel
- Kiểm tra bot có quyền "Connect" và "Speak" không
- Đảm bảo bot online và hoạt động

### Không phát được âm thanh
- Kiểm tra FFmpeg đã được cài đặt chưa
- Kiểm tra URL có hợp lệ không
- Kiểm tra bot có quyền phát audio không
- Đảm bảo file âm thanh không bị lỗi

### AI không trả lời
- Kiểm tra API key Google AI có hợp lệ không
- Kiểm tra kết nối internet

## 📁 Cấu trúc project

```
discord_dev/
├── main.py              # File chính của bot (phiên bản cũ)
├── main_enhanced.py     # File chính với tính năng phát âm thanh nâng cao
├── requirements.txt     # Dependencies Python
├── .env                # File cấu hình (tạo từ env_example.txt)
├── FFMPEG_SETUP.md     # Hướng dẫn cài đặt FFmpeg
├── README.md           # File này
└── discord.log         # Log file (tự động tạo)
```

## 🆕 Tính năng mới

### Phiên bản Enhanced (main_enhanced.py)
- **Hỗ trợ đa nguồn**: YouTube, SoundCloud, Spotify, direct audio links
- **File upload**: Phát âm thanh từ file được upload
- **Thông tin chi tiết**: Hiển thị nguồn âm thanh và thông tin đầy đủ
- **Xử lý lỗi tốt hơn**: Thông báo lỗi rõ ràng và hướng dẫn khắc phục

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Hãy tạo issue hoặc pull request.

## 📄 License

Project này được phát hành dưới MIT License.
