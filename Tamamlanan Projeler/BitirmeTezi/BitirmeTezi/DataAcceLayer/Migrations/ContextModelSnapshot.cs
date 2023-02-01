﻿// <auto-generated />
using System;
using DataAcceLayer.Concrete;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;

#nullable disable

namespace DataAcceLayer.Migrations
{
    [DbContext(typeof(Context))]
    partial class ContextModelSnapshot : ModelSnapshot
    {
        protected override void BuildModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "6.0.10")
                .HasAnnotation("Relational:MaxIdentifierLength", 128);

            SqlServerModelBuilderExtensions.UseIdentityColumns(modelBuilder, 1L, 1);

            modelBuilder.Entity("Entitylayer.Category", b =>
                {
                    b.Property<int>("CategoryID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    SqlServerPropertyBuilderExtensions.UseIdentityColumn(b.Property<int>("CategoryID"), 1L, 1);

                    b.Property<string>("CategoryDescription")
                        .IsRequired()
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("CategoryName")
                        .IsRequired()
                        .HasMaxLength(50)
                        .HasColumnType("nvarchar(50)");

                    b.Property<bool>("CategoryStatus")
                        .HasColumnType("bit");

                    b.HasKey("CategoryID");

                    b.ToTable("Categories");
                });

            modelBuilder.Entity("Entitylayer.Concrete.Announcement", b =>
                {
                    b.Property<int>("AnnouncementID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    SqlServerPropertyBuilderExtensions.UseIdentityColumn(b.Property<int>("AnnouncementID"), 1L, 1);

                    b.Property<string>("AnnouncementDesc")
                        .IsRequired()
                        .HasColumnType("nvarchar(max)");

                    b.Property<bool>("AnnouncementStatus")
                        .HasColumnType("bit");

                    b.Property<string>("AnnouncementTitle")
                        .IsRequired()
                        .HasMaxLength(25)
                        .HasColumnType("nvarchar(25)");

                    b.HasKey("AnnouncementID");

                    b.ToTable("announcements");
                });

            modelBuilder.Entity("Entitylayer.Concrete.Contact", b =>
                {
                    b.Property<int>("ContactId")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    SqlServerPropertyBuilderExtensions.UseIdentityColumn(b.Property<int>("ContactId"), 1L, 1);

                    b.Property<string>("ContacMessage")
                        .IsRequired()
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("ContactCompanyName")
                        .IsRequired()
                        .HasMaxLength(20)
                        .HasColumnType("nvarchar(20)");

                    b.Property<string>("ContactEmail")
                        .IsRequired()
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("ContactName")
                        .IsRequired()
                        .HasMaxLength(25)
                        .HasColumnType("nvarchar(25)");

                    b.Property<string>("ContactPhone")
                        .IsRequired()
                        .HasColumnType("nvarchar(max)");

                    b.Property<bool>("ContactStatus")
                        .HasColumnType("bit");

                    b.Property<string>("ContactSubject")
                        .IsRequired()
                        .HasMaxLength(20)
                        .HasColumnType("nvarchar(20)");

                    b.HasKey("ContactId");

                    b.ToTable("contacts");
                });

            modelBuilder.Entity("Entitylayer.Concrete.OurService", b =>
                {
                    b.Property<int>("OurServiceID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    SqlServerPropertyBuilderExtensions.UseIdentityColumn(b.Property<int>("OurServiceID"), 1L, 1);

                    b.Property<string>("OurServiceDesc")
                        .IsRequired()
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("OurServiceName")
                        .IsRequired()
                        .HasMaxLength(25)
                        .HasColumnType("nvarchar(25)");

                    b.Property<bool>("OurServiceStatus")
                        .HasColumnType("bit");

                    b.Property<string>("OurServiceimg")
                        .HasColumnType("nvarchar(max)");

                    b.HasKey("OurServiceID");

                    b.ToTable("ourServices");
                });

            modelBuilder.Entity("Entitylayer.Concrete.OurTeam", b =>
                {
                    b.Property<int>("OurTeamID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    SqlServerPropertyBuilderExtensions.UseIdentityColumn(b.Property<int>("OurTeamID"), 1L, 1);

                    b.Property<string>("OurTeamDescription")
                        .IsRequired()
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("OurTeamImage")
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("OurTeamInstagram")
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("OurTeamJob")
                        .IsRequired()
                        .HasMaxLength(20)
                        .HasColumnType("nvarchar(20)");

                    b.Property<string>("OurTeamLinkedIn")
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("OurTeamMail")
                        .HasColumnType("nvarchar(max)");

                    b.Property<string>("OurTeamName")
                        .IsRequired()
                        .HasMaxLength(25)
                        .HasColumnType("nvarchar(25)");

                    b.Property<bool>("OurTeamStatus")
                        .HasColumnType("bit");

                    b.HasKey("OurTeamID");

                    b.ToTable("ourTeams");
                });

            modelBuilder.Entity("Entitylayer.Work", b =>
                {
                    b.Property<int>("WorkID")
                        .ValueGeneratedOnAdd()
                        .HasColumnType("int");

                    SqlServerPropertyBuilderExtensions.UseIdentityColumn(b.Property<int>("WorkID"), 1L, 1);

                    b.Property<int>("CategoryID")
                        .HasColumnType("int");

                    b.Property<string>("WorkContent")
                        .IsRequired()
                        .HasColumnType("nvarchar(max)");

                    b.Property<DateTime>("WorkDate")
                        .HasColumnType("datetime2");

                    b.Property<string>("WorkImage")
                        .HasColumnType("nvarchar(max)");

                    b.Property<bool?>("WorkStatus")
                        .HasColumnType("bit");

                    b.Property<string>("WorkTitle")
                        .IsRequired()
                        .HasMaxLength(50)
                        .HasColumnType("nvarchar(50)");

                    b.HasKey("WorkID");

                    b.HasIndex("CategoryID");

                    b.ToTable("Works");
                });

            modelBuilder.Entity("Entitylayer.Work", b =>
                {
                    b.HasOne("Entitylayer.Category", "category")
                        .WithMany("works")
                        .HasForeignKey("CategoryID")
                        .OnDelete(DeleteBehavior.Cascade)
                        .IsRequired();

                    b.Navigation("category");
                });

            modelBuilder.Entity("Entitylayer.Category", b =>
                {
                    b.Navigation("works");
                });
#pragma warning restore 612, 618
        }
    }
}