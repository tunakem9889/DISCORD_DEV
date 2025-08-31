# Discord Bot với AI và Music Player

Một Discord bot đa chức năng với khả năng AI chat và phát nhạc từ YouTube.

## ✨ Tính năng chính

- **AI Chat**: Tích hợp Google Gemini AI để trả lời câu hỏi
- **Music Player**: Phát nhạc từ YouTube với queue system
- **Voice Commands**: Điều khiển nhạc qua voice channel
- **Auto-moderation**: Tự động xóa tin nhắn không phù hợp

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
python main.py
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
| `$play <URL>` | Phát nhạc từ YouTube | `$play https://youtube.com/watch?v=...` |
| `$search <từ khóa>` | Tìm kiếm và phát nhạc | `$search despacito` |
| `$audio` | Bot tham gia kênh thoại | `$audio` |
| `$skip` | Bỏ qua bài hát hiện tại | `$skip` |
| `$pause` | Tạm dừng bài hát | `$pause` |
| `$resume` | Tiếp tục phát bài hát | `$resume` |
| `$stop` | Dừng phát nhạc và xóa queue | `$stop` |
| `$queue` | Hiển thị danh sách phát | `$queue` |
| `$now` | Hiển thị bài hát đang phát | `$now` |
| `$remove <số>` | Xóa bài hát khỏi queue | `$remove 2` |
| `$shuffle` | Xáo trộn queue | `$shuffle` |
| `$volume [0-100]` | Điều chỉnh âm lượng | `$volume 80` |
| `$leave` | Bot rời khỏi kênh voice | `$leave` |

## 🎯 Cách sử dụng

### 1. Khởi động bot
```
python main.py
```

### 2. Tham gia voice channel
```
$audio
```

### 3. Phát nhạc
```
$play https://youtube.com/watch?v=...
```

### 4. Tìm kiếm nhạc
```
$search despacito
```

### 5. Điều khiển phát nhạc
```
$skip      # Bỏ qua bài hát
$pause     # Tạm dừng
$resume    # Tiếp tục
$stop      # Dừng hoàn toàn
```

### 6. Quản lý queue
```
$queue     # Xem danh sách
$remove 2  # Xóa bài hát thứ 2
$shuffle   # Xáo trộn
```

### 7. Hỏi AI
```
$start Bạn có thể làm gì?
```

## 🔧 Troubleshooting

### Bot không tham gia voice channel
- Kiểm tra bot có quyền "Connect" và "Speak" không
- Đảm bảo bot online và hoạt động

### Không phát được nhạc
- Kiểm tra FFmpeg đã được cài đặt chưa
- Kiểm tra URL YouTube có hợp lệ không
- Kiểm tra bot có quyền phát audio không

### AI không trả lời
- Kiểm tra API key Google AI có hợp lệ không
- Kiểm tra kết nối internet

## 📁 Cấu trúc project

```
discord_dev/
├── main.py              # File chính của bot
├── requirements.txt     # Dependencies Python
├── .env                # File cấu hình (tạo từ env_example.txt)
├── FFMPEG_SETUP.md     # Hướng dẫn cài đặt FFmpeg
├── README.md           # File này
└── discord.log         # Log file (tự động tạo)
```

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Hãy tạo issue hoặc pull request.

## 📄 License

Project này được phát hành dưới MIT License.
