# 🚀 Hướng dẫn sử dụng nhanh - Universal Audio Bot

## ⚡ Khởi động nhanh

### 1. Cài đặt
```bash
pip install -r requirements.txt
```

### 2. Cấu hình
Tạo file `.env` từ `env_example.txt` và điền:
```
DISCORD_TOKEN=your_discord_bot_token
GENAI_API_KEY=your_google_ai_api_key
```

### 3. Chạy bot
```bash
python main_enhanced.py
```

## 🎵 Sử dụng tính năng phát âm thanh

### Phát âm thanh từ URL
```
$play https://youtube.com/watch?v=...
$play https://soundcloud.com/...
$play https://open.spotify.com/track/...
$play https://example.com/audio.mp3
```

### Phát âm thanh từ file upload
1. Upload file âm thanh (.mp3, .wav, .flac, .m4a, .ogg)
2. Gõ lệnh: `$playfile`

### Tìm kiếm âm thanh
```
$search despacito
```

### Điều khiển phát
```
$skip      # Bỏ qua
$pause     # Tạm dừng
$resume    # Tiếp tục
$stop      # Dừng hoàn toàn
$queue     # Xem danh sách
$now       # Thông tin hiện tại
```

## 🌐 Hỗ trợ nguồn âm thanh

| Nguồn | Ví dụ URL | Tính năng |
|-------|-----------|-----------|
| **YouTube** | `https://youtube.com/watch?v=...` | Video, playlist |
| **SoundCloud** | `https://soundcloud.com/...` | Track, playlist |
| **Spotify** | `https://open.spotify.com/track/...` | Track, album |
| **Direct Audio** | `https://example.com/audio.mp3` | File âm thanh trực tiếp |
| **File Upload** | Upload file | .mp3, .wav, .flac, .m4a, .ogg |

## 🔧 Lệnh hữu ích

### Quản lý queue
```
$queue           # Xem danh sách
$remove 2        # Xóa âm thanh thứ 2
$shuffle         # Xáo trộn queue
$volume 80       # Điều chỉnh âm lượng
```

### Thông tin
```
$now             # Âm thanh đang phát
$helps           # Danh sách lệnh đầy đủ
```

### Voice channel
```
$audio           # Tham gia kênh voice
$leave           # Rời khỏi kênh voice
```

## ⚠️ Lưu ý quan trọng

1. **Bot cần quyền**: Connect, Speak, Attach Files
2. **FFmpeg**: Cần cài đặt FFmpeg để phát âm thanh
3. **File size**: File upload tối đa 25MB (giới hạn Discord)
4. **Format**: Hỗ trợ .mp3, .wav, .flac, .m4a, .ogg

## 🆘 Troubleshooting

### Bot không phát được âm thanh
- Kiểm tra bot có trong voice channel không
- Kiểm tra FFmpeg đã cài đặt chưa
- Kiểm tra URL có hợp lệ không

### File upload không hoạt động
- Kiểm tra định dạng file (.mp3, .wav, .flac, .m4a, .ogg)
- Kiểm tra kích thước file (< 25MB)
- Đảm bảo gõ lệnh `$playfile` sau khi upload

### Lỗi kết nối
- Kiểm tra internet connection
- Kiểm tra bot token có hợp lệ không
- Restart bot nếu cần

## 🎯 Ví dụ sử dụng

### Scenario 1: Phát nhạc từ YouTube
```
$play https://youtube.com/watch?v=dQw4w9WgXcQ
```

### Scenario 2: Upload file âm thanh
```
[Upload file song.mp3]
$playfile
```

### Scenario 3: Tìm kiếm và phát
```
$search despacito
```

### Scenario 4: Quản lý queue
```
$queue
$remove 1
$shuffle
$volume 90
```

## 📞 Hỗ trợ

Nếu gặp vấn đề:
1. Kiểm tra log file `discord.log`
2. Đảm bảo tất cả dependencies đã cài đặt
3. Kiểm tra quyền bot trong Discord server
4. Restart bot và thử lại
