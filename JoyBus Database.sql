USE [master]
GO

/****** Object:  Database [Bus Scheduler]    Script Date: 20/04/2024 10:59:44 am ******/
CREATE DATABASE [Bus Scheduler]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Bus Scheduler', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Bus Scheduler.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Bus Scheduler_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Bus Scheduler_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Bus Scheduler].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [Bus Scheduler] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [Bus Scheduler] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [Bus Scheduler] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [Bus Scheduler] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [Bus Scheduler] SET ARITHABORT OFF 
GO

ALTER DATABASE [Bus Scheduler] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [Bus Scheduler] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [Bus Scheduler] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [Bus Scheduler] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [Bus Scheduler] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [Bus Scheduler] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [Bus Scheduler] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [Bus Scheduler] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [Bus Scheduler] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [Bus Scheduler] SET  DISABLE_BROKER 
GO

ALTER DATABASE [Bus Scheduler] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [Bus Scheduler] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [Bus Scheduler] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [Bus Scheduler] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [Bus Scheduler] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [Bus Scheduler] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [Bus Scheduler] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [Bus Scheduler] SET RECOVERY FULL 
GO

ALTER DATABASE [Bus Scheduler] SET  MULTI_USER 
GO

ALTER DATABASE [Bus Scheduler] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [Bus Scheduler] SET DB_CHAINING OFF 
GO

ALTER DATABASE [Bus Scheduler] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [Bus Scheduler] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [Bus Scheduler] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [Bus Scheduler] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO

ALTER DATABASE [Bus Scheduler] SET QUERY_STORE = ON
GO

ALTER DATABASE [Bus Scheduler] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO

ALTER DATABASE [Bus Scheduler] SET  READ_WRITE 
GO


USE [Bus Scheduler]
GO
/****** Object:  Table [dbo].[Bus]    Script Date: 20/04/2024 11:01:03 am ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Bus](
	[BusCompanyName] [varchar](50) NOT NULL,
	[Origin] [varchar](50) NOT NULL,
	[Destination] [varchar](50) NOT NULL,
	[Time] [time](7) NOT NULL,
	[Fare] [int] NOT NULL
) ON [PRIMARY]
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'00:01:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'02:30:00' AS Time), 740)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'03:30:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'04:30:00' AS Time), 740)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'08:30:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'11:00:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'12:00:00' AS Time), 740)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'14:00:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'16:00:00' AS Time), 740)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'18:00:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'20:00:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'22:00:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Cubao', N'Baguio', CAST(N'23:00:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Pasay', N'Baguio', CAST(N'00:01:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Pasay', N'Baguio', CAST(N'01:30:00' AS Time), 760)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Pasay', N'Baguio', CAST(N'02:30:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Pasay', N'Baguio', CAST(N'03:30:00' AS Time), 760)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Pasay', N'Baguio', CAST(N'08:30:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Pasay', N'Baguio', CAST(N'10:00:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Pasay', N'Baguio', CAST(N'23:00:00' AS Time), 760)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Pasay', N'Baguio', CAST(N'13:00:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Pasay', N'Baguio', CAST(N'14:30:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Pasay', N'Baguio', CAST(N'16:00:00' AS Time), 760)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Pasay', N'Baguio', CAST(N'18:00:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Pasay', N'Baguio', CAST(N'21:30:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'00:00:00' AS Time), 760)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Trinoma', CAST(N'01:00:00' AS Time), 740)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Avenida', CAST(N'01:45:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'02:00:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'03:00:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Trinoma', CAST(N'05:00:00' AS Time), 740)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'06:00:00' AS Time), 760)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Trinoma', CAST(N'07:00:00' AS Time), 740)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'08:00:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'10:00:00' AS Time), 740)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Avenida', CAST(N'10:30:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Trinoma', CAST(N'11:00:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'12:00:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'14:00:00' AS Time), 740)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Avenida', CAST(N'14:00:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'16:00:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'18:00:00' AS Time), 760)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Trinoma', CAST(N'19:00:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'20:00:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'21:00:00' AS Time), 760)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Avenida', CAST(N'21:30:00' AS Time), 720)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Pasay', CAST(N'22:00:00' AS Time), 730)
GO
INSERT [dbo].[Bus] ([BusCompanyName], [Origin], [Destination], [Time], [Fare]) VALUES (N'JoyBus', N'Baguio', N'Avenida', CAST(N'22:30:00' AS Time), 720)
GO
