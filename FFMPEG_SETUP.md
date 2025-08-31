# Hướng dẫn cài đặt FFmpeg

FFmpeg là một công cụ xử lý audio cần thiết để Discord bot có thể phát nhạc từ YouTube và các nguồn khác.

**Lưu ý quan trọng:** Bot này chỉ hỗ trợ audio streaming, không có video streaming.

## 🪟 Windows

### Phương pháp 1: Sử dụng Chocolatey (Khuyến nghị)
1. Cài đặt Chocolatey nếu chưa có:
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```

2. Cài đặt FFmpeg:
   ```powershell
   choco install ffmpeg
   ```

### Phương pháp 2: Tải trực tiếp
1. Truy cập [FFmpeg Windows Builds](https://github.com/BtbN/FFmpeg-Builds/releases)
2. Tải file `ffmpeg-master-latest-win64-gpl.zip`
3. Giải nén vào thư mục (ví dụ: `C:\ffmpeg`)
4. Thêm `C:\ffmpeg\bin` vào PATH environment variable

### Phương pháp 3: Sử dụng winget
```powershell
winget install FFmpeg
```

## 🐧 Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install ffmpeg
```

## 🍎 macOS

### Sử dụng Homebrew (Khuyến nghị)
```bash
brew install ffmpeg
```

### Sử dụng MacPorts
```bash
sudo port install ffmpeg
```

## ✅ Kiểm tra cài đặt

Sau khi cài đặt, kiểm tra FFmpeg đã hoạt động:

```bash
ffmpeg -version
```

Nếu hiển thị thông tin phiên bản, FFmpeg đã được cài đặt thành công!

## 🔧 Kiểm tra hỗ trợ audio codec

Để đảm bảo bot có thể phát nhạc, kiểm tra FFmpeg có hỗ trợ các codec audio cần thiết:

```bash
ffmpeg -codecs | grep -E "(mp3|aac|opus)"
```

Nếu hiển thị các codec này, FFmpeg đã sẵn sàng cho audio streaming!

## 🚀 Khởi động lại

Sau khi cài đặt FFmpeg:
1. **Windows**: Khởi động lại Command Prompt hoặc PowerShell
2. **Linux/macOS**: Khởi động lại terminal hoặc chạy `source ~/.bashrc`

## 🔧 Troubleshooting

### FFmpeg không được nhận diện
- Kiểm tra PATH environment variable
- Khởi động lại terminal/command prompt
- Kiểm tra FFmpeg đã được cài đặt đúng cách

### Audio streaming không hoạt động
- Kiểm tra FFmpeg có hỗ trợ codec audio không
- Đảm bảo bot có quyền phát audio
- Kiểm tra kết nối internet

### Lỗi "FFmpeg not found"
- Cài đặt FFmpeg theo hướng dẫn trên
- Kiểm tra PATH environment variable
- Khởi động lại terminal sau khi cài đặt

## 📚 Tài liệu tham khảo

- [FFmpeg Official Website](https://ffmpeg.org/)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [FFmpeg Wiki](https://trac.ffmpeg.org/)

## 🆘 Hỗ trợ

Nếu gặp vấn đề với FFmpeg:
1. Kiểm tra log trong file `discord.log`
2. Chạy `ffmpeg -version` để xác nhận cài đặt
3. Kiểm tra PATH environment variable
4. Tạo issue trên GitHub repository
